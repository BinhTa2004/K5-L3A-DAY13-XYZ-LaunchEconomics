"""Kiểm toán chi phí, retry và mẫu số chỉ số; chạy: python -m unittest -v test_lab13."""
import contextlib
import io
import math
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

import lab13


class MoHinhNhoTests(unittest.TestCase):
    def setUp(self):
        # C là loại ngoài phạm vi, chi phí lớn để bắt lỗi quên lọc runs theo request_id.
        self.reqs = pd.DataFrame([
            ['A', 'noi_dia', 2, 'thanh_cong', 1, 'giu', 2, 0, 1, 0],
            ['B', 'hang_nang', 1, 'lam_lai', 1, 'sua', 3, 5, 0, 1],
            ['C', 'quoc_te', 1, 'thanh_cong', 0, '', 0, 0, 1, 0],
        ], columns=['request_id', 'loai', 'so_lan_chay', 'ket_qua', 'duoc_xem_lai',
                    'quyet_dinh_xem_lai', 'phut_xem_lai_simulated', 'phut_lam_lai_simulated',
                    'dong_trong_24h', 'mo_lai_trong_7_ngay'])
        self.runs = pd.DataFrame([
            ['A', 1, 1000, 100, 1, 'loi'],
            ['A', 2, 2000, 200, 2, 'ok'],
            ['B', 1, 1000, 300, 1, 'ok'],
            ['C', 1, 999000, 1000, 9, 'ok'],
        ], columns=['request_id', 'attempt', 'tokens_in', 'tokens_out', 'tool_calls', 'status'])

    def test_costs_include_failed_runs_but_only_selected_requests(self):
        kq = lab13.mo_hinh(self.runs, self.reqs.iloc[:2])
        # Tính tay: token = (26+13)+(52+26)+(26+39); tool = (1+2+1)*15.
        self.assertAlmostEqual(kq['token'], 182)
        self.assertEqual(kq['tool'], 60)
        self.assertAlmostEqual(kq['chay_lai'], 108)
        self.assertEqual(kq['xem_lai'], 10_000)
        self.assertEqual(kq['lam_lai'], 10_000)
        self.assertEqual(kq['tong'], 20_242)
        self.assertEqual(kq['thanh_cong'], 1)
        self.assertEqual(kq['cps'], 20_242)
        self.assertEqual(kq['hoa_don_moi_yc'], 121)
        self.assertEqual(kq['chi_phi_he_thong'], 32_242)

    def test_retry_cap_reclassifies_and_clears_human_time_without_mutating_inputs(self):
        reqs_goc, runs_goc = self.reqs.copy(deep=True), self.runs.copy(deep=True)
        kq = lab13.mo_hinh(self.runs, self.reqs.iloc[:2], max_lan_chay=1)
        self.assertEqual(kq['so_lan_chay'], 2)
        self.assertEqual(kq['thanh_cong'], 0)
        self.assertEqual(kq['xem_lai'], 6000)
        self.assertEqual(kq['lam_lai'], 10_000)
        self.assertEqual(kq['tong'], 16_134)
        self.assertEqual(kq['chi_phi_he_thong'], 40_134)
        self.assertTrue(math.isinf(kq['cps']))
        assert_frame_equal(self.reqs, reqs_goc)
        assert_frame_equal(self.runs, runs_goc)
        self.assertEqual(lab13.mo_hinh(self.runs, self.reqs.iloc[:2])['thanh_cong'], 1)
        with self.assertRaises(ValueError):
            lab13.mo_hinh(self.runs, self.reqs.iloc[:0])

    def test_fixed_cost_uses_whole_population_not_only_eligible_requests(self):
        kq = lab13.chi_phi_co_dinh(self.runs, self.reqs, yeu_cau_thang=300, co_dinh=10_000)
        # 1 thành công trong phạm vi / 3 yêu cầu toàn mẫu, không phải 1/2.
        self.assertEqual(kq['thanh_cong_thang'], 100)
        self.assertEqual(kq['co_dinh_moi_viec'], 100)
        self.assertEqual(kq['cps_cong_co_dinh'], 20_342)

    def test_full_review_counts_distinct_requests_with_ok_and_replaces_existing_time(self):
        self.runs.loc[0, 'status'] = 'ok'  # Hai run ok của A vẫn chỉ tính một lượt xem.
        kq = lab13.xem_lai_100(self.runs, self.reqs, phut_lam_lai=9)
        self.assertEqual(kq['duoc_xem'], 2)
        self.assertEqual(kq['so_lam_lai'], 1)
        self.assertEqual(kq['xem_lai'], 20_000)
        self.assertEqual(kq['lam_lai'], 18_000)
        self.assertEqual(kq['tong'], 38_242)
        self.assertEqual(kq['cps'], 38_242)

    def test_metric_denominators_and_no_review_case(self):
        # Một giá trị sua trên ca không được xem lại không được lọt vào tử số bỏ qua.
        self.reqs.loc[2, 'quyet_dinh_xem_lai'] = 'sua'
        kq = lab13.tinh_chi_so(self.reqs)
        self.assertEqual(kq['chinh']['tu_so'], 2)
        self.assertEqual(kq['chinh']['mau_so'], 3)
        self.assertEqual(kq['bo_qua'], dict(tu_so=1, mau_so=2, ti_le=0.5))
        self.assertEqual(kq['an_toan']['tu_so'], 1)
        self.reqs['duoc_xem_lai'] = 0
        self.assertTrue(math.isnan(lab13.tinh_chi_so(self.reqs)['bo_qua']['ti_le']))


class RetryTests(unittest.TestCase):
    def test_known_answers_and_probability_boundaries(self):
        with contextlib.redirect_stdout(io.StringIO()):
            lab13.kiem_tra_dap_an_biet_truoc()
        for k in (1, 2, 3, 10):
            for p in (0.1, 0.5, 0.8, 1):
                with self.subTest(k=k, p=p):
                    # E[N] = tổng P(N >= j), kiểm bằng cách độc lập với công thức thương.
                    self.assertAlmostEqual(lab13.so_lan_chay_ky_vong(p, k),
                                           sum((1 - p) ** j for j in range(k)))
                    self.assertAlmostEqual(lab13.he_so_chi_phi_moi_viec_thanh_cong(p, k), 1 / p)
        self.assertEqual(lab13.so_lan_chay_ky_vong(0, 3), 3)
        self.assertEqual(lab13.ti_le_thanh_cong(0), 0)
        self.assertTrue(math.isinf(lab13.so_lan_chay_ky_vong(0)))
        self.assertTrue(math.isinf(lab13.he_so_chi_phi_moi_viec_thanh_cong(0, 3)))

    def test_invalid_probability_and_attempt_limits(self):
        for ham in (lab13.so_lan_chay_ky_vong, lab13.ti_le_thanh_cong,
                    lab13.he_so_chi_phi_moi_viec_thanh_cong):
            for p, k in [(-0.1, 2), (1.1, 2), (math.nan, 2), (0.8, 0),
                         (0.8, -1), (0.8, 1.5), (0.8, True)]:
                with self.subTest(ham=ham.__name__, p=p, k=k), self.assertRaises(ValueError):
                    ham(p, k)


class DoiChieuDuLieuLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs, cls.reqs = lab13.doc_du_lieu()

    def test_a2_a3_a4_match_reference_and_preserve_empty_decisions(self):
        self.assertEqual((len(self.runs), len(self.reqs)), (1624, 1200))
        self.assertEqual(self.reqs['quyet_dinh_xem_lai'].isna().sum(), 0)
        kq = lab13.mo_hinh(self.runs, self.reqs)
        for key, expected in {'token': 245_585, 'tool': 84_000, 'chay_lai': 93_804,
                              'xem_lai': 1_780_000, 'lam_lai': 2_264_000,
                              'tong': 4_373_585, 'cps': 4472}.items():
            self.assertAlmostEqual(kq[key], expected, delta=0.5, msg=key)
        self.assertEqual(kq['thanh_cong'], 978)
        for loai, expected in {'noi_dia': 2696, 'hang_nang': 8221,
                               'quoc_te': 22_515, 'doi_tac': 10_215}.items():
            phan = self.reqs.loc[self.reqs['loai'].eq(loai)]
            self.assertAlmostEqual(lab13.mo_hinh(self.runs, phan)['cps'], expected, delta=0.5)
        full = lab13.chi_phi_co_dinh(self.runs, self.reqs)
        half = lab13.chi_phi_co_dinh(self.runs, self.reqs, yeu_cau_thang=22_500)
        self.assertEqual(full['thanh_cong_thang'], 33_750)
        self.assertAlmostEqual(full['cps_cong_co_dinh'], 4599, delta=0.5)
        self.assertAlmostEqual(half['cps_cong_co_dinh'], 5784, delta=0.5)
        self.assertAlmostEqual(half['co_dinh_moi_viec'], full['co_dinh_moi_viec'] * 2)

    def test_b1_reference_symmetry_and_b2_additivity(self):
        kq = lab13.bang_do_nhay(self.runs, self.reqs)
        self.assertEqual(len(kq), 9)
        for row, expected in zip(kq, [4723, 4346, 6292, 3562, 6787, 3315, 5506, 4237, 4111]):
            self.assertAlmostEqual(row['cps'], expected, delta=0.5)
        for i in (0, 2, 4):
            self.assertAlmostEqual(kq[i]['thay_doi'], -2 * kq[i + 1]['thay_doi'])
        cap = lab13.mo_hinh(self.runs, self.reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
        goc = lab13.mo_hinh(self.runs, self.reqs)
        self.assertAlmostEqual(cap['cps'] - goc['cps'],
                               (kq[0]['cps'] - goc['cps']) + (kq[2]['cps'] - goc['cps']))

    def test_b3_system_cost_and_success_cost_have_different_optima(self):
        rows = [lab13.mo_hinh(self.runs, self.reqs, max_lan_chay=k) for k in (1, 2, 3)]
        for row, failed, total in zip(rows, [319, 234, 222], [7_449_781, 6_901_220, 7_037_585]):
            self.assertEqual(row['khong_thanh_cong'], failed)
            self.assertAlmostEqual(row['chi_phi_he_thong'], total, delta=0.5)
        self.assertEqual(min(range(3), key=lambda i: rows[i]['chi_phi_he_thong']) + 1, 2)
        self.assertEqual(min(range(3), key=lambda i: rows[i]['cps']) + 1, 1)

    def test_b4_and_e_reference(self):
        b4 = lab13.xem_lai_100(self.runs, self.reqs)
        self.assertEqual((b4['so_yeu_cau'], b4['duoc_xem'], b4['so_lam_lai'], b4['thanh_cong']),
                         (982, 948, 48, 900))
        self.assertAlmostEqual(b4['cps'], 11_743, delta=0.5)
        phut_tb = self.reqs.loc[self.reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
        conservative = lab13.xem_lai_100(self.runs, self.reqs, phut_lam_lai=phut_tb)
        self.assertAlmostEqual(conservative['cps'], 12_414.5, delta=0.01)
        self.assertLess(b4['cps'], lab13.BASELINE)
        self.assertGreater(conservative['cps'], lab13.BASELINE)
        e = lab13.tinh_chi_so(self.reqs)
        for key, num, den in [('chinh', 994, 1200), ('bo_qua', 48, 177), ('an_toan', 51, 1200)]:
            self.assertEqual(e[key], dict(tu_so=num, mau_so=den, ti_le=num / den))

    def test_cli_sections_and_top_three_use_distinct_factors(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            lab13.main()
        output = buf.getvalue()
        for section in ('A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'E1'):
            self.assertIn(section + ' ·', output)
        line = next(line for line in output.splitlines() if line.startswith('Ba yếu tố'))
        self.assertIn('1. Số ca làm lại gấp đôi', line)
        self.assertIn('2. Tỉ lệ xem lại gấp đôi', line)
        self.assertIn('3. Lương nhân viên tăng 25%', line)


if __name__ == '__main__':
    unittest.main()
