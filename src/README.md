# Source code

Code bài làm và dữ liệu giả lập của Lab 13. **Mọi lệnh bên dưới chạy trong thư mục `src/`.**

- File bắt đầu chạy: `lab13.py` (file nộp; Bình đã triển khai A–B và phép tính ba chỉ số E). `lab13_starter.py` là bản khởi đầu để đối chiếu, không sửa.
- Cách chạy: `python3 lab13.py`.
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, file yêu cầu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`.
- Output hiện tại: ba phép thử A1, bảng A2–A4, B1–B4, tỉ lệ run ok theo lần thử và ba chỉ số E1. Kết quả in dưới dạng bảng để Long kiểm và chép vào hồ sơ. Các chi phí dùng phút nhân viên giả lập đều có nhãn `simulated`.
- D1 chưa triển khai: Minh bổ sung hàm tính cỡ mẫu và gọi trong `main()` tại dòng `TODO CP4`; giữ nguyên A–B và lời gọi `in_chi_so(reqs)` đã có.
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
| `lab13.py` | Code A1–A4, B1–B4 và phép tính ba chỉ số E1; còn `TODO CP4` cho D1 |
| `test_lab13.py` | 12 bài kiểm tra công thức retry, chi phí, giới hạn chạy, mẫu số chỉ số và đối chiếu dữ liệu lab |
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

## Kiểm tra và bàn giao phần Bình

```powershell
python lab13.py
python -m unittest -v test_lab13
```

Code và kiểm tra A–B/E1 hiện chỉ cần `pandas`; bộ thư viện đầy đủ của lab vẫn cài theo `requirements.txt`. Đầu vào được đọc theo vị trí `lab13.py` nên chạy từ root repo bằng `python src/lab13.py` cũng được. Chương trình xuất UTF-8 để giữ đúng tiếng Việt trên Windows.

- Long: chạy lệnh trên để đối chiếu và điền `bang_chi_phi.md`, `chi_so.md`; chưa coi kiểm tra tự động là lượt kiểm độc lập của Long.
- Minh: nhận code này trước khi viết D1. `mo_hinh()` không sửa dữ liệu đầu vào và tự lọc runs theo tập yêu cầu, nên có thể dùng lại cho phạm vi pilot.
- A4 coi 45.000 là tổng mọi loại yêu cầu, phân bổ cố định theo tỉ lệ thành công trong phạm vi trên toàn mẫu. B3 cộng 12.000 đ cho mỗi yêu cầu không thành công theo quy ước lab.
- B4 xem lại một lần cho mỗi yêu cầu có ít nhất một run `ok`; hai dòng dùng 9 phút/ca và trung bình chính xác của cột `phut_lam_lai_simulated` trên mọi ca `lam_lai`. Các bảng B chưa cộng cố định; B4 chưa cộng chi phí chuyển nhân viên.
