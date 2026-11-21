# Báo cáo cá nhân — Tạ Công Bình — 2A202603628

## 1. Thông tin thành viên

- Họ tên: Tạ Công Bình; MSSV: 2A202603628; GitHub: BinhTa2004.
- Vai: người viết code A–B/E1, trưởng nhóm và tích hợp bài.
- Trạng thái: code chạy đủ A–B–D1–E1, hồ sơ chung đã tích hợp và tự chấm 98/100.

## 2. Phần việc phụ trách

Viết A1–A4/B1–B4 và phép tính ba chỉ số E1, bàn giao cho Long kiểm và Minh bổ sung D1; tích hợp bài, kiểm gói nộp và cập nhật bằng chứng.

## 3. Đóng góp cụ thể

- `4bdce40`: ba hàm retry A1; `mo_hinh` tính mọi run và lọc theo request; bảng A3/A4, chín kịch bản B1, B2, chi phí hệ thống B3 và hai giả định B4; ba chỉ số E1 có tử/mẫu số; 12 kiểm tra ban đầu.
- Tích hợp code D1 của Minh (`99aa565`, `60def4d`), bộ nhãn Dũng (`0a72f5f`), bảng số và kiểm D1 của Long (`19cb5be`, `093ec85`); mốc gộp `f3c48a4`.
- Bổ sung power ở mức +5/+6, so sánh chi phí có cả cố định và phần nhân viên; thêm bốn kiểm tra tích hợp và script kiểm số csv/Decimal.
- Đối chiếu hồ sơ từng người, thống nhất tên sự kiện với luật dừng và tổng hợp báo cáo nhóm từ kết quả tính toán. Giữ nguyên CSV, bản khởi đầu và bộ nhãn của Dũng.

## 4. Bằng chứng và kết quả

[Code](../../src/lab13.py), [kiểm tra](../../src/test_lab13.py), [script kiểm số](../../src/kiem_so_doc_lap.py), [output](ket_qua_tinh_toan.txt), [JSON kiểm độc lập](kiem_so_doc_lap.json), [báo cáo nhóm](group_report.md). Chạy trong `src/` bằng Python 3.12.9:

```powershell
.\.venv\Scripts\python.exe lab13.py
.\.venv\Scripts\python.exe -m unittest -v test_lab13
.\.venv\Scripts\python.exe kiem_so_doc_lap.py
```

16/16 kiểm tra đạt; A1 là 1,20 · 1,25 · 1,25. Đối chiếu chi phí bằng Decimal không import mô hình chính khớp sai số <0,000001 đ; công thức z kiểm D1 sai khác statsmodels <0,25%.

| Chỉ tiêu | Kết quả |
| --- | --- |
| A2 | Tổng 4.373.585,13 đ /978 =4.471,97 đ/việc [simulated] |
| So đầy đủ trong phạm vi | Hệ thống + cố định 5.217,09 đ/yêu cầu ở 45.000 yêu cầu/tháng [simulated] |
| B2 | Token và xem lại cùng tăng: 6.543,12 đ, +46,31% [simulated] |
| B3 | 2 lần chạy rẻ nhất cho hệ thống: 6.901.220,23 đ; 1 lần cho CPS thấp nhất [simulated] |
| B4 | 11.742,79 hoặc 12.414,50 đ/việc theo giả định phút làm lại [simulated] |
| D1 | 5.980 mẫu thô/nhánh, 859,20 hiệu dụng; power +6=0,8010, +5=0,6418 |
| E1 | 994/1.200=82,83%; 48/177=27,12%; 51/1.200=4,25% |

## 5. Công cụ AI và cách kiểm tra

ChatGPT/Codex hỗ trợ code, kiểm tra, tích hợp và báo cáo. Kiểm lại bằng ví dụ tính tay, công thức z và Decimal từ CSV; chương trình không gọi model thật.

## 6. Tự đánh giá

Code chạy đủ các phần và có thể kiểm lại từ CSV. Thời gian nhân viên chiếm 92,46% tổng chi phí [simulated], nên việc giảm xem lại và làm lại có ảnh hưởng lớn hơn giảm giá token. Trước pilot cần kiểm chống hoàn trùng, bật log, đo thời gian thật và thống nhất MDE.

Hạn chế chính là dữ liệu thời gian còn giả lập và chưa có đối chứng thực tế. Nhóm đã tự chấm 98/100; C3 trừ 2 điểm do bằng chứng khóa bộ nhãn 1 chưa đầy đủ.
