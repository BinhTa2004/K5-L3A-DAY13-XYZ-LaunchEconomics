"""Kiểm số A/E/D1 bằng csv, Decimal và công thức z; không import lab13/pandas.

Bổ sung khi rà soát chung bằng Codex, không coi là script gốc Long đã dùng.
Chạy: python kiem_so_doc_lap.py. Toàn bộ dữ liệu giả lập của lab.
"""
import csv
from decimal import Decimal
import json
import math
from pathlib import Path
from statistics import NormalDist


def kiem_so():
    folder = Path(__file__).resolve().parent
    with (folder / 'logix_runs.csv').open(encoding='utf-8', newline='') as f:
        runs = list(csv.DictReader(f))
    with (folder / 'logix_requests.csv').open(encoding='utf-8', newline='') as f:
        reqs = list(csv.DictReader(f))

    def tinh_chi_phi(requests):
        ids = {r['request_id'] for r in requests}
        selected = [r for r in runs if r['request_id'] in ids]
        token = sum((Decimal(r['tokens_in']) * 26 + Decimal(r['tokens_out']) * 130)
                    / 1000 for r in selected)
        tool = sum(int(r['tool_calls']) * 15 for r in selected)
        review = sum(Decimal(r['phut_xem_lai_simulated']) * 2000 for r in requests)
        rework = sum(Decimal(r['phut_lam_lai_simulated']) * 2000 for r in requests)
        success = sum(r['ket_qua'] == 'thanh_cong' for r in requests)
        total = token + tool + review + rework
        return dict(requests=len(requests), runs=len(selected), success=success,
                    token=float(token), tool=tool, review=float(review), rework=float(rework),
                    total=float(total), cps=float(total / success),
                    system_per_request=float((total + (len(requests) - success) * 12000) / len(requests)))

    by_type = {kind: tinh_chi_phi([r for r in reqs if r['loai'] == kind])
               for kind in sorted({r['loai'] for r in reqs})}
    scope_reqs = [r for r in reqs if r['loai'] in ('noi_dia', 'hang_nang')]
    scope = tinh_chi_phi(scope_reqs)
    fixed_per_scope_request = 40_000_000 / (45_000 * len(scope_reqs) / len(reqs))
    reviewed = [r for r in reqs if r['duoc_xem_lai'] == '1']
    e = dict(primary_count=sum(r['dong_trong_24h'] == '1' and r['mo_lai_trong_7_ngay'] == '0' for r in reqs),
             ignored_count=sum(r['quyet_dinh_xem_lai'] in ('sua', 'bo') for r in reviewed),
             reviewed_count=len(reviewed), reopened_count=sum(r['mo_lai_trong_7_ngay'] == '1' for r in reqs),
             denominator=len(reqs))
    za, zb = NormalDist().inv_cdf(0.975), NormalDist().inv_cdf(0.8)
    p1, p2 = 0.70, 0.75
    pb = (p1 + p2) / 2
    n = math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                   + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)
    m = math.ceil(859 * 0.98 / (20 - 859 * 0.02))
    d = dict(n_per_arm_z=n, design_effect_75=2.48, raw_per_arm_75=math.ceil(n * 2.48),
             staff_per_arm=math.ceil(n * 2.48 / 75), effective_staff_limit=1000,
             effective_depot_limit=300, requests_per_staff_for_6pp=m,
             effective_sample_for_6pp=20 * m / (1 + (m - 1) * 0.02))
    return dict(method='stdlib csv + Decimal + NormalDist; no import of lab13',
                simulated=True, all_requests=tinh_chi_phi(reqs), by_type=by_type,
                scope=scope, scope_system_including_fixed_per_request=scope['system_per_request'] + fixed_per_scope_request,
                metrics=e, d1=d)


if __name__ == '__main__':
    print(json.dumps(kiem_so(), ensure_ascii=True, indent=2, allow_nan=False))
