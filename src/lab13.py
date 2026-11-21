"""Lab 13 · Chi phí A–B và ba chỉ số E, tính trực tiếp từ CSV.

Chạy trong src/: python lab13.py. Phần này chỉ cần pandas, không gọi API.
Mọi chi phí có thời gian nhân viên giả lập được ghi nhãn simulated.
Nguồn công thức: docs/du_lieu_va_cong_thuc.md và hướng dẫn chi tiết Lab 13.
Bản khởi đầu giữ nguyên ở lab13_starter.py; phần D1 do Minh bổ sung.
"""
import math
import sys
from numbers import Integral
from pathlib import Path

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000
YEU_CAU_THANG = 45_000
PHAM_VI_PILOT = ('noi_dia', 'hang_nang')


def doc_du_lieu():
    """Đọc cạnh file code; ô quyết định trống phải giữ là chuỗi trống."""
    thu_muc = Path(__file__).resolve().parent
    runs = pd.read_csv(thu_muc / 'logix_runs.csv')
    reqs = pd.read_csv(thu_muc / 'logix_requests.csv', keep_default_na=False)
    return runs, reqs


def _kiem_tra_gioi_han(k):
    if k is not None and (isinstance(k, bool) or not isinstance(k, Integral) or k < 1):
        raise ValueError('Giới hạn chạy phải là số nguyên dương hoặc None.')


def _kiem_tra_xac_suat(p, k):
    if not 0 <= p <= 1:
        raise ValueError('Xác suất p phải nằm trong [0, 1].')
    _kiem_tra_gioi_han(k)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    _kiem_tra_xac_suat(p, k)
    if p == 0:
        return math.inf if k is None else float(k)
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    _kiem_tra_xac_suat(p, k)
    if p == 0:
        return 0.0
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    _kiem_tra_gioi_han(max_lan_chay)
    if reqs.empty:
        raise ValueError('Cần ít nhất một yêu cầu để tính mô hình chi phí.')
    # Copy để các kịch bản không sửa dữ liệu gốc hoặc ảnh hưởng lần gọi sau.
    reqs = reqs.copy()
    runs = runs.loc[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs.loc[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = float(tien_token.sum()), float(tien_tool.sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    khong_thanh_cong = len(reqs) - thanh_cong
    # Quy ước B3 của lab: mọi yêu cầu không thành công được nhân viên xử lý 12.000đ.
    chi_phi_he_thong = tong + BASELINE * khong_thanh_cong
    return dict(
        token=token, tool=tool,
        chay_lai=float((tien_token + tien_tool).loc[runs['attempt'] > 1].sum()),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
        thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(token + tool) / len(reqs),
        so_yeu_cau=len(reqs), so_lan_chay=len(runs), khong_thanh_cong=khong_thanh_cong,
        chi_phi_he_thong=chi_phi_he_thong,
        he_thong_moi_yc=chi_phi_he_thong / len(reqs),
    )


def chi_phi_co_dinh(runs, reqs, yeu_cau_thang=YEU_CAU_THANG, co_dinh=CO_DINH_THANG):
    """45.000 là tổng mọi loại; chỉ phân bổ cố định cho số thành công trong phạm vi."""
    if yeu_cau_thang <= 0 or co_dinh < 0:
        raise ValueError('Khối lượng phải dương và chi phí cố định không âm.')
    pham_vi = reqs.loc[reqs['loai'].isin(PHAM_VI_PILOT)]
    kq = mo_hinh(runs, pham_vi)
    thanh_cong_thang = yeu_cau_thang * kq['thanh_cong'] / len(reqs)
    co_dinh_moi_viec = co_dinh / thanh_cong_thang if thanh_cong_thang else math.inf
    return dict(yeu_cau_thang=yeu_cau_thang, thanh_cong_thang=thanh_cong_thang,
                co_dinh_moi_viec=co_dinh_moi_viec, cps_bien_doi=kq['cps'],
                cps_cong_co_dinh=kq['cps'] + co_dinh_moi_viec)


def bang_do_nhay(runs, reqs):
    """B1: đổi từng yếu tố, luôn tính lại trên cùng dữ liệu chưa bị sửa."""
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=LUONG_PHUT * 1.25),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    cps_goc = mo_hinh(runs, reqs)['cps']
    ket_qua = []
    for ten, tham_so in kich_ban.items():
        kq = mo_hinh(runs, reqs, **tham_so)
        ket_qua.append(dict(ten=ten, **kq, thay_doi=kq['cps'] / cps_goc - 1))
    return ket_qua


def xem_lai_100(runs, reqs, phut_lam_lai=9, phut_xem_lai=5):
    """B4: xem lại một lần/yêu cầu có ít nhất một run ok, không tính theo số run."""
    pham_vi = reqs.loc[reqs['loai'].isin(PHAM_VI_PILOT)]
    runs_pham_vi = runs.loc[runs['request_id'].isin(pham_vi['request_id'])]
    duoc_xem = int(runs_pham_vi.loc[runs_pham_vi['status'].eq('ok'), 'request_id'].nunique())
    so_lam_lai = int(pham_vi['ket_qua'].eq('lam_lai').sum())
    goc = mo_hinh(runs_pham_vi, pham_vi)
    xem_lai = duoc_xem * phut_xem_lai * LUONG_PHUT
    lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
    tong = goc['token'] + goc['tool'] + xem_lai + lam_lai
    hoa_von = ((BASELINE * goc['thanh_cong'] - goc['token'] - goc['tool'] - lam_lai)
               / (duoc_xem * LUONG_PHUT)) if duoc_xem else math.nan
    return dict(so_yeu_cau=len(pham_vi), duoc_xem=duoc_xem, so_lam_lai=so_lam_lai,
                phut_lam_lai=phut_lam_lai, token_tool=goc['token'] + goc['tool'],
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=goc['thanh_cong'],
                cps=tong / goc['thanh_cong'] if goc['thanh_cong'] else math.inf,
                phut_xem_lai_hoa_von=hoa_von)


def tinh_chi_so(reqs):
    """E1: trả cả tử số, mẫu số; mẫu số 0 được báo không xác định."""
    duoc_xem = reqs.loc[reqs['duoc_xem_lai'].eq(1)]
    dem = {
        'chinh': (int((reqs['dong_trong_24h'].eq(1) & reqs['mo_lai_trong_7_ngay'].eq(0)).sum()), len(reqs)),
        'bo_qua': (int(duoc_xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()), len(duoc_xem)),
        'an_toan': (int(reqs['mo_lai_trong_7_ngay'].eq(1).sum()), len(reqs)),
    }
    return {ten: dict(tu_so=tu, mau_so=mau, ti_le=tu / mau if mau else math.nan)
            for ten, (tu, mau) in dem.items()}


def _so(value, le=0):
    if math.isnan(value):
        return 'không xác định'
    if math.isinf(value):
        return 'vô hạn'
    return f'{value:,.{le}f}'.replace(',', '_').replace('.', ',').replace('_', '.')


def _phan_tram(value, le=2):
    return _so(value * 100, le) + '%' if math.isfinite(value) else _so(value)


def _in_bang(tieu_de, cot, dong):
    print(f'\n{tieu_de}')
    print('| ' + ' | '.join(cot) + ' |')
    print('| ' + ' | '.join('---' for _ in cot) + ' |')
    for hang in dong:
        print('| ' + ' | '.join(str(o) for o in hang) + ' |')


def in_phan_a(runs, reqs):
    goc = mo_hinh(runs, reqs)
    _in_bang('A1 · p = 0,8', ['Phép thử', 'Kết quả'], [
        ['Số lần chạy, tối đa 2 lần', _so(so_lan_chay_ky_vong(0.8, 2), 2)],
        ['Số lần chạy, đến khi đúng', _so(so_lan_chay_ky_vong(0.8), 2)],
        ['Hệ số chi phí, tối đa 3 lần', _so(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 2)],
    ])
    cac_khoan = [('Token', 'token', 'đo từ trace'), ('Tool', 'tool', 'đo từ trace'),
                 ('Trong đó: token + tool lần 2, 3', 'chay_lai', 'đo từ trace; không cộng lần nữa'),
                 ('Xem lại', 'xem_lai', 'simulated'), ('Làm lại', 'lam_lai', 'simulated'),
                 ('Tổng chi phí', 'tong', 'simulated'), ('Số việc thành công', 'thanh_cong', 'số yêu cầu'),
                 ('Chi phí mỗi việc thành công', 'cps', 'simulated'),
                 ('Hóa đơn token + tool / yêu cầu', 'hoa_don_moi_yc', 'đo từ trace')]
    _in_bang('A2 · Mô hình chi phí (đ)', ['Khoản', 'Giá trị', 'Nhãn'],
             [[ten, _so(goc[key], 2), nhan] for ten, key, nhan in cac_khoan])
    print(f"CPS / hóa đơn mỗi yêu cầu = {_so(goc['cps'] / goc['hoa_don_moi_yc'], 2)} lần [simulated].")
    print(f"Làm lại chiếm {_phan_tram(goc['lam_lai'] / goc['tong'])}; "
          f"giờ nhân viên chiếm {_phan_tram((goc['xem_lai'] + goc['lam_lai']) / goc['tong'])} [simulated].")
    print(f"Chi phí cả hệ thống / yêu cầu = {_so(goc['he_thong_moi_yc'], 2)} đ "
          f"= {_so(goc['he_thong_moi_yc'] / BASELINE, 2)} lần nhân viên tự làm [simulated; chưa có cố định].")

    dong = []
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        phan = reqs.loc[reqs['loai'].eq(loai)]
        if phan.empty:
            continue
        kq = mo_hinh(runs, phan)
        dong.append([loai, kq['so_yeu_cau'], _phan_tram(kq['thanh_cong'] / len(phan)),
                     _so(kq['so_lan_chay'] / len(phan), 2), _so(kq['cps'], 2),
                     _so(kq['cps'] / BASELINE, 2)])
    _in_bang('A3 · Theo loại yêu cầu; chi phí simulated, chưa có cố định',
             ['Loại', 'Yêu cầu', 'Thành công', 'Lần chạy / yêu cầu', 'CPS (đ)', 'CPS / 12.000'], dong)
    theo_lan = runs.merge(reqs[['request_id', 'loai']], on='request_id', validate='many_to_one')
    dong = []
    for (loai, lan), phan in theo_lan.groupby(['loai', 'attempt'], sort=True):
        ok = int(phan['status'].eq('ok').sum())
        dong.append([loai, lan, f'{ok}/{len(phan)}', _phan_tram(ok / len(phan))])
    _in_bang('A3 bổ sung · Run ok theo lần thử (khác với yêu cầu thành công cuối cùng)',
             ['Loại', 'Lần thử', 'Run ok / run', 'Tỉ lệ ok'], dong)

    dong = []
    for khoi_luong in (YEU_CAU_THANG, YEU_CAU_THANG / 2):
        kq = chi_phi_co_dinh(runs, reqs, khoi_luong)
        dong.append([_so(khoi_luong), _so(kq['thanh_cong_thang']), _so(kq['co_dinh_moi_viec'], 2),
                     _so(kq['cps_cong_co_dinh'], 2), _so(kq['cps_cong_co_dinh'] / BASELINE, 2)])
    _in_bang('A4 · noi_dia + hang_nang, cộng 40 triệu đ/tháng [simulated]',
             ['Tổng yêu cầu / tháng', 'Thành công phạm vi / tháng', 'Cố định / việc (đ)',
              'CPS + cố định (đ)', 'CPS / 12.000'], dong)
    print('A4 phân bổ theo tỷ trọng thành công trong toàn mẫu; so sánh vận hành phải tính cả phần chuyển nhân viên như B3.')


def in_phan_b(runs, reqs):
    goc = mo_hinh(runs, reqs)
    do_nhay = bang_do_nhay(runs, reqs)
    _in_bang('B1 · Chín kịch bản, chưa có cố định [simulated]', ['Kịch bản', 'CPS (đ)', 'Thay đổi'],
             [[kq['ten'], _so(kq['cps'], 2), _phan_tram(kq['thay_doi'])] for kq in do_nhay])
    cap = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2, he_so_xem_lai=2)
    print(f"\nB2 · Token và xem lại gấp đôi: {_so(cap['cps'], 2)} đ, "
          f"thay đổi {_phan_tram(cap['cps'] / goc['cps'] - 1)} [simulated].")
    # Xếp các mức tăng để không đếm cả tăng và giảm của cùng một yếu tố.
    xep_hang = sorted((kq for kq in do_nhay if kq['thay_doi'] > 0),
                      key=lambda x: x['thay_doi'], reverse=True)[:3]
    print('Ba yếu tố ảnh hưởng mạnh nhất: ' + '; '.join(
        f"{i}. {kq['ten']} ({_phan_tram(kq['thay_doi'])})" for i, kq in enumerate(xep_hang, 1)) + ' [simulated].')
    bang_gioi_han = {k: mo_hinh(runs, reqs, max_lan_chay=k) for k in (1, 2, 3)}
    _in_bang('B3 · Chi phí cả hệ thống theo quy ước lab; chưa có cố định [simulated]',
             ['Giới hạn', 'Tổng trợ lý (đ)', 'Không thành công', 'Cả hệ thống (đ)', 'CPS (đ)'],
             [[k, _so(kq['tong'], 2), kq['khong_thanh_cong'], _so(kq['chi_phi_he_thong'], 2),
               _so(kq['cps'], 2)] for k, kq in bang_gioi_han.items()])
    re_nhat = min(bang_gioi_han, key=lambda k: bang_gioi_han[k]['chi_phi_he_thong'])
    cps_thap = min(bang_gioi_han, key=lambda k: bang_gioi_han[k]['cps'])
    print(f'Rẻ nhất cho công ty: {re_nhat} lần; CPS thấp nhất: {cps_thap} lần [simulated].')

    phut_tb = float(reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean())
    b4 = [xem_lai_100(runs, reqs, phut) for phut in (9, phut_tb)]
    _in_bang('B4 · Xem lại mọi yêu cầu có run ok trong noi_dia + hang_nang, 5 phút/lần [simulated]',
             ['Phút làm lại / ca', 'Yêu cầu xem lại', 'Ca làm lại', 'Tổng (đ)', 'CPS (đ)',
              'CPS / 12.000', 'Phút xem lại hòa vốn'],
             [[_so(kq['phut_lam_lai'], 4), kq['duoc_xem'], kq['so_lam_lai'], _so(kq['tong'], 2),
               _so(kq['cps'], 2), _so(kq['cps'] / BASELINE, 2), _so(kq['phut_xem_lai_hoa_von'], 2)]
              for kq in b4])
    print('Dòng 1 dùng giả định đề 9 phút; dòng 2 dùng trung bình chính xác của mọi ca lam_lai trong CSV [simulated].')
    print('B4 chưa có cố định hay chi phí chuyển nhân viên; cần đo thời gian và khả năng giảm xem lại trong pilot.')


def tinh_co_mau_d1(reqs=None, baseline=0.70, mde=0.05, alpha=0.05, power=0.80, icc=0.02,
                   m_nhan_vien=75, cum_nhan_vien=20, cum_depot=6, n_muc_tieu_6_diem=859):
    """D1: tính cỡ mẫu theo ba cách chia (yêu cầu, nhân viên, depot) và mức chênh 6 điểm."""
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize

    p2 = baseline + mde
    h = proportion_effectsize(p2, baseline)
    n_yeu_cau_raw = float(NormalIndPower().solve_power(effect_size=h, alpha=alpha, power=power, ratio=1.0))
    n_yeu_cau = math.ceil(n_yeu_cau_raw)

    deff_b = 1 + (m_nhan_vien - 1) * icc
    n_nhom_b = math.ceil(n_yeu_cau * deff_b)
    nhan_vien_moi_nhom_b = math.ceil(n_nhom_b / m_nhan_vien)

    max_neff_nhan_vien = cum_nhan_vien / icc
    max_neff_depot = cum_depot / icc

    m_min_e = math.ceil(n_muc_tieu_6_diem * (1 - icc) / (cum_nhan_vien - n_muc_tieu_6_diem * icc))
    deff_e = 1 + (m_min_e - 1) * icc
    n_nhom_e = cum_nhan_vien * m_min_e
    neff_e = n_nhom_e / deff_e

    kq = dict(
        n_yeu_cau_raw=n_yeu_cau_raw, n_yeu_cau=n_yeu_cau,
        deff_b=deff_b, n_nhom_b=n_nhom_b, nhan_vien_moi_nhom_b=nhan_vien_moi_nhom_b,
        tong_nhan_vien_b=2 * nhan_vien_moi_nhom_b,
        max_neff_nhan_vien=max_neff_nhan_vien, max_neff_depot=max_neff_depot,
        m_min_e=m_min_e, deff_e=deff_e, n_nhom_e=n_nhom_e, neff_e=neff_e,
    )
    if reqs is not None:
        pham_vi = reqs.loc[reqs['loai'].isin(PHAM_VI_PILOT)]
        kq.update(
            mo_lai_toan_mau=float(reqs['mo_lai_trong_7_ngay'].mean()),
            mo_lai_pham_vi=float(pham_vi['mo_lai_trong_7_ngay'].mean()),
            mo_lai_noi_dia=float(reqs.loc[reqs['loai'].eq('noi_dia'), 'mo_lai_trong_7_ngay'].mean()),
            mo_lai_hang_nang=float(reqs.loc[reqs['loai'].eq('hang_nang'), 'mo_lai_trong_7_ngay'].mean()),
        )
    return kq


def in_phan_d(reqs):
    kq = tinh_co_mau_d1(reqs)
    _in_bang('D1 · Cỡ mẫu pilot (baseline 0,70; MDE +5 điểm; alpha 0,05; power 0,80; ICC 0,02)',
             ['Câu', 'Cách chia / bài toán', 'Kết quả'], [
                 ['a', 'Chia theo từng yêu cầu', f"{_so(kq['n_yeu_cau'])} yêu cầu/nhóm (raw {_so(kq['n_yeu_cau_raw'], 2)})"],
                 ['b', 'Chia theo nhân viên, m = 75',
                  f"DEFF = {_so(kq['deff_b'], 2)}; {_so(kq['n_nhom_b'])}/nhóm; "
                  f"{kq['nhan_vien_moi_nhom_b']} NV/nhóm (tổng {kq['tong_nhan_vien_b']} > 40 -> không đủ)"],
                 ['c', '20 nhân viên/nhóm, m tùy ý',
                  f"n_eff tối đa < {_so(kq['max_neff_nhan_vien'])}/nhóm (< {_so(kq['n_yeu_cau'])} -> không đạt câu a)"],
                 ['d', '6 depot/nhóm, m tùy ý',
                  f"n_eff tối đa < {_so(kq['max_neff_depot'])}/nhóm (< {_so(kq['n_yeu_cau'])} và < 20 cụm/nhóm)"],
                 ['e', 'MDE +6 điểm (cần 859/nhóm), 20 NV/nhóm',
                  f"m >= {kq['m_min_e']} YC/NV (DEFF = {_so(kq['deff_e'], 2)}; "
                  f"{_so(kq['n_nhom_e'])}/nhóm; n_eff = {_so(kq['neff_e'], 1)})"],
             ])
    print(f"Tỉ lệ mo_lai_trong_7_ngay chạy thử: toàn mẫu {_phan_tram(kq['mo_lai_toan_mau'])}; "
          f"phạm vi noi_dia + hang_nang {_phan_tram(kq['mo_lai_pham_vi'])} "
          f"(noi_dia {_phan_tram(kq['mo_lai_noi_dia'])}, hang_nang {_phan_tram(kq['mo_lai_hang_nang'])}).")


def in_chi_so(reqs):
    chi_so = tinh_chi_so(reqs)
    ten = {'chinh': 'Đóng trong 24h, không mở lại 7 ngày',
           'bo_qua': 'Sửa hoặc bỏ / được xem lại', 'an_toan': 'Mở lại trong 7 ngày / tổng yêu cầu'}
    _in_bang('E1 · Chỉ số trong đợt chạy thử (toàn bộ dữ liệu là giả lập)',
             ['Chỉ số', 'Tử số', 'Mẫu số', 'Tỉ lệ'],
             [[ten[key], kq['tu_so'], kq['mau_so'], _phan_tram(kq['ti_le'])] for key, kq in chi_so.items()])
    print('Đợt chạy thử không có đối chứng; các tỉ lệ này không chứng minh tác động của trợ lý.')


def main():
    runs, reqs = doc_du_lieu()
    print(f'Lab 13 · {len(reqs)} yêu cầu, {len(runs)} lần chạy; dữ liệu giả lập.')
    kiem_tra_dap_an_biet_truoc()
    in_phan_a(runs, reqs)
    in_phan_b(runs, reqs)
    in_phan_d(reqs)
    in_chi_so(reqs)


if __name__ == '__main__':
    # Python trên Windows có thể dùng cp1252 khi stdout được chuyển vào pipe/file.
    sys.stdout.reconfigure(encoding='utf-8')
    main()
