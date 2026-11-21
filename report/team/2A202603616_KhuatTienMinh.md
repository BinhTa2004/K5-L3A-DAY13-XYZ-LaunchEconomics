# Báo cáo cá nhân — Khuất Tiến Minh — 2A202603616

## 1. Thông tin thành viên

- Họ tên: Khuất Tiến Minh; MSSV: 2A202603616; GitHub: Minhktm02.
- Vai: người gắn nhãn 1; bảng lỗi C, code D1 sau giải lao và kế hoạch pilot D.
- Trạng thái: đã bàn giao C/D1/YAML (`99aa565`), nhận main (`60def4d`), Long kiểm ở `093ec85`; phần lịch/gate/power được hoàn thiện khi tích hợp.

## 2. Phần việc phụ trách

Gắn 20 ca trước khi so với Dũng, giữ nhãn gốc; tính đồng thuận và khắc phục đủ năm loại; thêm D1 mà giữ nguyên A–B/E1 của Bình; hoàn thiện thiết kế pilot, cỡ mẫu và luật dừng.

## 3. Đóng góp cụ thể

Theo báo cáo bàn giao: Minh đọc đề và gắn bộ 1 trước khi xem tham khảo, dùng bộ Dũng `0a72f5f` để so, đạt 20/20; hoàn thiện năm cách khắc phục và quy tắc phân biệt ca 13/9/7–8. Repo lưu bảng hai bộ ở `99aa565`; thời điểm/độc lập là khai báo thành viên, chưa có file khóa riêng bộ 1 trong repo để xác nhận lại bằng lịch sử trước khi so.

Minh thêm `tinh_co_mau_d1`/`in_phan_d` dùng statsmodels, tính cả tỉ lệ mở lại toàn mẫu/phạm vi và hoàn thiện YAML chia staff 20+20, MDE +6, DE 6,96, 5.980 mẫu thô/nhóm.

Lần tích hợp cuối có Codex bổ sung power ở tác động +5/+6, phân biệt mẫu thô/hiệu dụng, lịch đề xuất có đủ 7 ngày theo dõi, gate hoàn trùng tức thời và metric/event thống nhất. Không quy các bổ sung này thành công việc Minh đã tự làm ở commit ban đầu.

## 4. Bằng chứng và kết quả

[Bảng C](bang_loi.md), [pilot](pilot_plan.yaml), [code](../../src/lab13.py), [output](ket_qua_tinh_toan.txt), [kiểm độc lập](kiem_so_doc_lap.json). Commit gốc `99aa565`, tích hợp `60def4d`; giữ nguyên [nhãn Dũng](nhan_dung_doc_lap.md).

D1: 1.250 yêu cầu/nhóm; DE 2,48, 3.100 yêu cầu/nhóm và 42 người/nhóm (tổng 84>40); trần 20 staff/nhóm <1.000, 6 depot/nhóm <300. Với +6 điểm: 20×299=5.980, DE 6,96, n_eff=859,1954; power +6=0,8010, +5=0,6418. Công thức z cho 1.251/3.103, sai khác <0,25%.

Lịch giả định: khởi chạy 01/12/2026, đủ 20 người can thiệp từ 15/12, thu mẫu 15–28/12, theo dõi đến 04/01/2027, quyết định 05/01. Thiếu 299 yêu cầu ở bất kỳ người nào thì không mở rộng vì thiếu mẫu, không đổi MDE sau khi xem dữ liệu. YAML có bốn luật dừng; 16 kiểm tra tích hợp đạt.

## 5. Công cụ AI và kiểm tra

Theo khai báo ban đầu: Antigravity/Gemini hỗ trợ đọc DOCX, môi trường, code D1, YAML/checklist. Codex hỗ trợ lần rà soát chung. Kiểm bằng công thức z, csv/Decimal, statsmodels, `yaml.safe_load` và bộ kiểm tra; nhãn được giữ nguyên, không tạo nhãn độc lập mới sau khi đã so.

## 6. Đánh giá từ hồ sơ và việc tiếp theo

C/D đã có sản phẩm và số tái lập; cần giải thích đánh đổi MDE, ảnh hưởng spillover và vì sao n_eff không thể vượt trần c/ICC. Đồng thuận 100% không tự chứng minh tính độc lập; thành viên chịu trách nhiệm về quy trình gắn nhãn đã khai báo. Trước pilot cần roster đủ 40 người ở 12 depot; không dùng mẫu 20 người/6 depot để tự dựng roster. Đọc lại các gate/lịch mới, phối hợp duyệt chéo và tự nộp LMS.
