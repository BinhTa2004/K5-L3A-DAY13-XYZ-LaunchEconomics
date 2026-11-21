# Báo cáo cá nhân — Hoàng Hải Long — 2A202603670

## 1. Thông tin thành viên

- Họ tên: Hoàng Hải Long; MSSV: 2A202603670; GitHub: hwangron.
- Vai: người kiểm số; bảng chi phí A–B, chỉ số/event và rủi ro E1–E2; kiểm D1.
- Trạng thái: phần A–B/E và lượt kiểm D1 đã bàn giao (`19cb5be`, `093ec85`); schema và báo cáo được bổ sung trong lần tích hợp cuối.

## 2. Phần việc phụ trách

Đối chiếu ít nhất một khoản bằng cách độc lập, hoàn thiện bảng A1–A4/B1–B4, ba chỉ số thử/hai chỉ số thêm/event/rủi ro và kiểm cỡ mẫu của Minh.

## 3. Đóng góp cụ thể

Phần bàn giao gồm kiểm token, tool, thời gian xem lại/làm lại, CPS toàn mẫu và nhóm quoc_te bằng script riêng; điền bảng chi phí, ba chỉ số tính thử, hai chỉ số đề xuất, chín sự kiện và ba rủi ro. Commit `093ec85` ghi kết quả kiểm D1 bằng công thức z và ba góp ý cho YAML.

Bản tích hợp có 14 sự kiện, bổ sung thời điểm và khóa để đo các luật dừng. Phần so sánh chi phí tính thêm cố định. [Script csv/Decimal](../../src/kiem_so_doc_lap.py) được thêm khi tích hợp để lưu kết quả kiểm số độc lập; đây là script bổ sung, khác với script đã dùng ở bước bàn giao.

## 4. Bằng chứng và kết quả

[Bảng chi phí](bang_chi_phi.md), [chỉ số/event](chi_so.md), [kết quả kiểm độc lập](kiem_so_doc_lap.json), [output mô hình](ket_qua_tinh_toan.txt). Commit gốc `19cb5be`, lượt kiểm D1 `093ec85`.

- Token =5.771.712/1.000×26 +734.774/1.000×130 =245.585,13 đ; tool =5.600×15 =84.000 đ. Xem lại 890×2.000=1.780.000 đ, làm lại 1.132×2.000=2.264.000 đ [simulated].
- CPS =4.373.585,13/978=4.471,97 đ [simulated], khớp mô hình; làm lại +51,77%, xem lại +40,70%, lương +23,12% [simulated].
- D1 theo z: 1.251 và 3.103, so statsmodels 1.250 và 3.100, đều sai khác <0,25%; 42 người/nhánh, trần hiệu dụng 1.000 hoặc 300, m>=299 cho +6 điểm.
- Phần tích hợp chạy 16/16 kiểm tra đạt; `yaml.safe_load` đọc được. Power 0,8010 ở +6 nhưng 0,6418 ở +5; không bỏ qua số bất lợi.

## 5. Công cụ AI và kiểm tra

Claude Code hỗ trợ kiểm số và phần A–B/E; ChatGPT/Codex hỗ trợ đặc tả sự kiện, script Decimal và báo cáo khi tích hợp. Số liệu đối chiếu từ CSV và công thức lab.

## 6. Tự đánh giá

Bảng chi phí và D1 đã được đối chiếu; các chỉ số đều có sự kiện làm nguồn tính. Hạn chế là thời gian simulated, ICC giả định và chưa có đối chứng thực tế. Tỉ lệ 82,83% chưa chứng minh trợ lý nâng chất lượng; cần đo thời gian và kiểm toán số tiền trong pilot.
