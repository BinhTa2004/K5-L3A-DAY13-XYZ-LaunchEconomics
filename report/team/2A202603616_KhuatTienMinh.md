# Báo cáo cá nhân — Khuất Tiến Minh — 2A202603616

## 1. Thông tin thành viên

- Họ tên: Khuất Tiến Minh; MSSV: 2A202603616; GitHub: Minhktm02.
- Vai: người gắn nhãn 1; bảng lỗi C, code D1 sau giải lao và kế hoạch pilot D.
- Trạng thái: đã bàn giao C/D1/YAML (`99aa565`), nhận main (`60def4d`), Long kiểm ở `093ec85`; phần lịch/gate/power được hoàn thiện khi tích hợp.

## 2. Phần việc phụ trách

Gắn 20 ca trước khi so với Dũng, giữ nhãn gốc; tính đồng thuận và khắc phục đủ năm loại; thêm D1 mà giữ nguyên A–B/E1 của Bình; hoàn thiện thiết kế pilot, cỡ mẫu và luật dừng.

## 3. Đóng góp cụ thể

Phần C gồm bộ nhãn 1, bảng so với bộ nhãn của Dũng (`0a72f5f`), năm cách khắc phục và quy tắc phân biệt ca 13/9/7–8. Hai bộ khớp 20/20, được lưu trong `99aa565`. Nguồn và ghi chú về quy trình gắn nhãn nằm trong [bảng C](bang_loi.md).

Minh thêm `tinh_co_mau_d1`/`in_phan_d` dùng statsmodels, tính cả tỉ lệ mở lại toàn mẫu/phạm vi và hoàn thiện YAML chia staff 20+20, MDE +6, DE 6,96, 5.980 mẫu thô/nhóm.

Khi tích hợp, kế hoạch được bổ sung power ở mức +5/+6, phân biệt mẫu thô và hiệu dụng, lịch theo dõi đủ 7 ngày và luật dừng ngay khi hoàn trùng. Các sự kiện dùng để đo được thống nhất với phần E.

## 4. Bằng chứng và kết quả

[Bảng C](bang_loi.md), [pilot](pilot_plan.yaml), [code](../../src/lab13.py), [output](ket_qua_tinh_toan.txt), [kiểm độc lập](kiem_so_doc_lap.json). Commit gốc `99aa565`, tích hợp `60def4d`; giữ nguyên [nhãn Dũng](nhan_dung_doc_lap.md).

D1: 1.250 yêu cầu/nhóm; DE 2,48, 3.100 yêu cầu/nhóm và 42 người/nhóm (tổng 84>40); trần 20 staff/nhóm <1.000, 6 depot/nhóm <300. Với +6 điểm: 20×299=5.980, DE 6,96, n_eff=859,1954; power +6=0,8010, +5=0,6418. Công thức z cho 1.251/3.103, sai khác <0,25%.

Lịch giả định: khởi chạy 01/12/2026, đủ 20 người can thiệp từ 15/12, thu mẫu 15–28/12, theo dõi đến 04/01/2027, quyết định 05/01. Thiếu 299 yêu cầu ở bất kỳ người nào thì không mở rộng vì thiếu mẫu, không đổi MDE sau khi xem dữ liệu. YAML có bốn luật dừng; 16 kiểm tra tích hợp đạt.

## 5. Công cụ AI và kiểm tra

Antigravity/Gemini hỗ trợ D1 và YAML; ChatGPT/Codex hỗ trợ power, lịch, luật dừng và báo cáo. Kiểm lại bằng công thức z, statsmodels, csv/Decimal và `yaml.safe_load`.

## 6. Tự đánh giá

Phần C/D đã có bảng kết quả và code chạy được. Điểm hạn chế của thiết kế là phải tăng MDE lên +6 điểm; nếu tác động thực chỉ +5 thì power còn 0,6418. Trước pilot cần chốt danh sách 40 nhân viên ở 12 depot; mẫu CSV chỉ có 20 người ở 6 depot nên chưa đủ để lập danh sách phân nhóm.
