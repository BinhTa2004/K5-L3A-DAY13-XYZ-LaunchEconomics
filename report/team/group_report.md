# Báo cáo nhóm XYZ · Lab 13 · L3A

## 1. Thông tin nhóm

Nhóm XYZ gồm Tạ Công Bình (2A202603628), Hoàng Hải Long (2A202603670), Khuất Tiến Minh (2A202603616), Nguyễn Tuấn Dũng (2A202603608). Repo: [K5-L3A-DAY13-XYZ-LaunchEconomics](https://github.com/BinhTa2004/K5-L3A-DAY13-XYZ-LaunchEconomics), nhánh `main`; vai và commit tại [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí, lỗi và thiết kế pilot trợ lý hoàn phí LogiX-VN trên 1.200 yêu cầu/1.624 run giả lập. Chi phí cộng mọi lần chạy kể cả lỗi, mẫu số chỉ đếm việc thành công; so với nhân viên bằng chi phí cả hệ thống trên cùng số yêu cầu.

## 3. Giải pháp

A–B: code tái lập và [bảng chi phí](bang_chi_phi.md), 9 kịch bản độ nhạy, chạy lại 1–3 lần và review 100%. C: [bảng lỗi](bang_loi.md) giữ hai cột nhãn, 5 cách khắc phục. D: [pilot](pilot_plan.yaml) ngẫu nhiên staff 20+20, đối chứng đồng thời. E: [chỉ số/event](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md). Đầu ra lưu tại [kết quả tính](ket_qua_tinh_toan.txt); [script kiểm số](../../src/kiem_so_doc_lap.py) dùng csv/Decimal, không gọi mô hình chính.

## 4. Kết quả

CPS 4.471,97 đ; giờ nhân viên chiếm 92,46% [simulated]. Giới hạn 2 lần cho tổng hệ thống thấp nhất 6.901.220,23 đ [simulated], dù 1 lần cho CPS thấp nhất. Trong phạm vi noi_dia + hang_nang, hệ thống có cố định là 5.217,09 đ/yêu cầu ở đủ tải [simulated].

Review 100% cho CPS 11.742,79–12.414,50 đ tùy phút làm lại, chưa có cố định/chuyển nhân viên [simulated]. Ba chỉ số toàn mẫu: 82,83%, 27,12%, 4,25%; không suy tác động nhân quả từ đợt không có đối chứng. Hai cột nhãn hiện khớp 20/20; tính độc lập theo khai báo và nguồn trong bảng C.

Pilot chấp nhận MDE +6 điểm: 5.980 mẫu thô/nhóm, DE 6,96, hiệu dụng 859,20; power 0,8010 ở +6 nhưng chỉ 0,6418 ở +5. Bốn luật dừng và lịch đề xuất 01/12/2026–05/01/2027 đã viết trước. Nhóm đề xuất **Go có điều kiện**, chỉ phạm vi nội địa/hàng nặng; điều kiện an toàn, event và đo phút phải đạt trước khi chạy. **Duyệt chéo chưa diễn ra**, theo xác nhận của Bình; [phiếu](phieu_cham.md) đang chờ, chưa có điểm hội đồng.

## 5. Khó khăn và cách xử lý

Máy tích hợp thiếu statsmodels; tạo `.venv`, cài thư viện đã khai báo và chạy đủ A–B–D1–E1. Python Windows dùng cp1252 khi xuất qua pipe; code đặt UTF-8. Phân biệt 5.980 mẫu thô với 859 hiệu dụng, thống nhất thời gian theo dõi 7 ngày và bổ sung event cho guardrail. Không sửa CSV hoặc bản starter.

## 6. Tổng hợp đóng góp

| Thành viên | Phần đã bàn giao | Bằng chứng gốc |
| --- | --- | --- |
| Bình | A–B/E1, kiểm tra, tích hợp | `4bdce40`, `f3c48a4` |
| Long | Bảng chi phí, chỉ số/event, kiểm D1 | `19cb5be`, `093ec85` |
| Minh | C, code D1, kế hoạch pilot | `99aa565`, `60def4d` |
| Dũng | Khung launch, bộ nhãn 2, giữ hồ sơ | `fb2023d`, `0a72f5f` |

Lần hoàn thiện chung có ChatGPT/Codex hỗ trợ bổ sung power, kiểm chi phí, schema event và tổng hợp báo cáo; không quy toàn bộ phần này thành công việc cá nhân đã tự làm trước đó. Báo cáo từng người ghi rõ phạm vi hỗ trợ AI.

## 7. Hạn chế và hướng cải thiện

16/16 kiểm tra tự động đạt và đối chiếu độc lập khớp; không thay thế lượt duyệt chéo hoặc bằng chứng đã sửa hệ thống thật. Thời gian là simulated, ICC/mức nền là giả định; cần đo thật, kiểm spillover, đủ 20 cụm mỗi nhánh và 299 yêu cầu/người. Thời điểm gắn nhãn độc lập theo khai báo thành viên. Mỗi người còn phải đọc, giải thích phần mình và tự nộp LMS; chưa xác nhận việc nộp.

## 8. Tài liệu tham khảo

[Quy tắc và công thức lab](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), đề bài `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, [rubric](../../RUBRIC.md). Không gọi model thật hoặc dùng API key trong bài tính.
