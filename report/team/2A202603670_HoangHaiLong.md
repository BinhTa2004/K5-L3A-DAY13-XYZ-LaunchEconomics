# Báo cáo cá nhân — Hoàng Hải Long — 2A202603670

## 1. Thông tin thành viên

- Họ tên: Hoàng Hải Long; MSSV: 2A202603670; GitHub: hwangron.
- Vai: người kiểm số; bảng chi phí A–B, chỉ số/event và rủi ro E1–E2; kiểm D1.
- Trạng thái: phần A–B/E và lượt kiểm D1 đã bàn giao (`19cb5be`, `093ec85`); schema và báo cáo được bổ sung trong lần tích hợp cuối.

## 2. Phần việc phụ trách

Đối chiếu ít nhất một khoản bằng cách độc lập, hoàn thiện bảng A1–A4/B1–B4, ba chỉ số thử/hai chỉ số thêm/event/rủi ro và kiểm cỡ mẫu của Minh.

## 3. Đóng góp cụ thể

Theo bản bàn giao của Long: dùng script riêng kiểm token/tool/xem lại/làm lại/CPS và quoc_te, không gọi `lab13.py`; điền toàn bộ bảng chi phí, ba chỉ số, hai chỉ số đề xuất, chín event và ba rủi ro. `093ec85` ghi kiểm D1 bằng z chính xác và ba góp ý cho YAML.

Lần hoàn thiện chung có Codex bổ sung 14 event/khóa/thời gian còn thiếu để đo được các luật dừng, so chi phí cùng mẫu số có cố định, và tạo [script csv/Decimal](../../src/kiem_so_doc_lap.py). Script bổ sung này độc lập với `lab13.py`, không được coi là script gốc Long đã dùng.

## 4. Bằng chứng và kết quả

[Bảng chi phí](bang_chi_phi.md), [chỉ số/event](chi_so.md), [kết quả kiểm độc lập](kiem_so_doc_lap.json), [output mô hình](ket_qua_tinh_toan.txt). Commit gốc `19cb5be`, lượt kiểm D1 `093ec85`.

- Token =5.771.712/1.000×26 +734.774/1.000×130 =245.585,13 đ; tool =5.600×15 =84.000 đ. Xem lại 890×2.000=1.780.000 đ, làm lại 1.132×2.000=2.264.000 đ [simulated].
- CPS =4.373.585,13/978=4.471,97 đ [simulated], khớp mô hình; làm lại +51,77%, xem lại +40,70%, lương +23,12% [simulated].
- D1 theo z: 1.251 và 3.103, so statsmodels 1.250 và 3.100, đều sai khác <0,25%; 42 người/nhánh, trần hiệu dụng 1.000 hoặc 300, m>=299 cho +6 điểm.
- Phần tích hợp chạy 16/16 kiểm tra đạt; `yaml.safe_load` đọc được. Power 0,8010 ở +6 nhưng 0,6418 ở +5; không bỏ qua số bất lợi.

## 5. Công cụ AI và kiểm tra

Theo báo cáo gốc, Claude Code (Claude Opus) hỗ trợ đọc đề, script và soạn A–B/E; kiểm từ CSV, output và công thức nguồn. Codex hỗ trợ rà soát cuối và script Decimal lưu trong repo; số được tạo bằng chạy code, không sửa tay artifact kết quả. Các lượt hỗ trợ được phân biệt với việc cá nhân tự thực hiện.

## 6. Đánh giá từ hồ sơ và việc tiếp theo

Đã có bảng số, kiểm D1 và contract event đủ cho chỉ số/gate. Hạn chế là phút simulated, ICC giả định và chưa có đối chứng thật; 82,83% không chứng minh trợ lý nâng chất lượng. Cần đọc lại schema mới, kiểm phút thật và audit tiền trước pilot; hỗ trợ Dũng bảo vệ chi phí và tự nộp LMS.
