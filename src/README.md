# Source code

Code bài làm và dữ liệu giả lập của Lab 13. **Mọi lệnh bên dưới chạy trong thư mục `src/`.**

- File bắt đầu chạy: `lab13.py` (file nộp; Bình triển khai A–B/E1, Minh bổ sung D1). `lab13_starter.py` là bản khởi đầu để đối chiếu, không sửa.
- Cách chạy: `python3 lab13.py`.
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, file yêu cầu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`.
- Output hiện tại: ba phép thử A1, bảng A2–A4, B1–B4, tỉ lệ run ok theo lần thử, D1 và power ở tác động +5/+6, ba chỉ số E1. Kết quả in dưới dạng bảng để Long kiểm và chép vào hồ sơ. Các chi phí dùng phút nhân viên giả lập đều có nhãn `simulated`.
- D1 đã tích hợp: `tinh_co_mau_d1(reqs)` và `in_phan_d(reqs)` của Minh; `main()` chạy đủ A–B–D1–E1. Mẫu thô 5.980/nhóm khác với hiệu dụng 859,20; power +5 chỉ 0,6418.
- File học viên được sửa: `lab13.py`. Không sửa hai file CSV.

## Cài đặt

Cần Python 3.10 trở lên. Lab không cần khoá API và không cần mạng trong lúc làm.

macOS / Linux:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Lệnh `python -c` kiểm tra thư viện phải in ra `san sang`.

## File trong thư mục

| File | Nội dung |
| --- | --- |
| `lab13.py` | A1–A4, B1–B4, D1/power và ba chỉ số E1 |
| `test_lab13.py` | 16 kiểm tra retry/chi phí/chỉ số, D1, power, cỡ mẫu và lịch YAML |
| `kiem_so_doc_lap.py` | Kiểm A/E/D1 bằng csv, Decimal và NormalDist, không import mô hình chính |
| `lab13_starter.py` | Bản gốc của `lab13.py`, giữ nguyên để đối chiếu. Tài liệu trong `docs/` gọi file này là "file khởi đầu" |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu hoàn phí |
| `requirements.txt` | Thư viện cần cài |

Ý nghĩa từng cột và các công thức: [docs/du_lieu_va_cong_thuc.md](../docs/du_lieu_va_cong_thuc.md).

## Đọc dữ liệu đúng cách

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Thiếu `keep_default_na=False`, ô trống trong cột `quyet_dinh_xem_lai` bị đọc thành `NaN` và các phép so sánh phía sau sai.

## Kiểm tra bản tích hợp

```powershell
python lab13.py
python -m unittest -v test_lab13
python kiem_so_doc_lap.py
```

Bản tích hợp cần `pandas`, `statsmodels` và `pyyaml`; cài đủ theo `requirements.txt`. Trên máy này dùng `.\.venv\Scripts\python.exe` thay `python` nếu chưa activate môi trường. Đầu vào được đọc theo vị trí `lab13.py` nên chạy từ root repo bằng `python src/lab13.py` cũng được. Chương trình xuất UTF-8 để giữ đúng tiếng Việt trên Windows.

- Long đã bàn giao bảng số và kiểm D1; output tính toán được lưu trong `report/team/ket_qua_tinh_toan.txt`, kiểm độc lập bổ sung trong `report/team/kiem_so_doc_lap.json`.
- D1 đã có; `mo_hinh()` không sửa dữ liệu đầu vào và tự lọc runs theo tập yêu cầu. Không thay code mới bằng bản cũ khi tiếp tục sửa.
- A4 coi 45.000 là tổng mọi loại yêu cầu, phân bổ cố định theo tỉ lệ thành công trong phạm vi trên toàn mẫu. B3 cộng 12.000 đ cho mỗi yêu cầu không thành công theo quy ước lab.
- B4 xem lại một lần cho mỗi yêu cầu có ít nhất một run `ok`; hai dòng dùng 9 phút/ca và trung bình chính xác của cột `phut_lam_lai_simulated` trên mọi ca `lam_lai`. Các bảng B chưa cộng cố định; B4 chưa cộng chi phí chuyển nhân viên.

Script kiểm độc lập và artifact kết quả được bổ sung trong lượt rà soát chung có Codex hỗ trợ. Đây là kiểm số tái lập, không thay lượt duyệt chéo hoặc xác nhận hệ thống pilot đã vận hành.
