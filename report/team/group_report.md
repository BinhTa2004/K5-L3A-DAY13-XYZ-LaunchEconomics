# Báo cáo nhóm XYZ · Lab 13 · L3A

## 1. Thông tin nhóm

Nhóm XYZ gồm Tạ Công Bình (2A202603628), Hoàng Hải Long (2A202603670), Khuất Tiến Minh (2A202603616), Nguyễn Tuấn Dũng (2A202603608). Repo: [K5-L3A-DAY13-XYZ-LaunchEconomics](https://github.com/BinhTa2004/K5-L3A-DAY13-XYZ-LaunchEconomics), nhánh `main`; vai và commit tại [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm phân tích 1.200 yêu cầu và 1.624 lần chạy giả lập để đánh giá chi phí và lập kế hoạch pilot cho trợ lý hoàn phí LogiX-VN. Chi phí tính cả lần chạy lỗi, còn số việc thành công chỉ gồm các yêu cầu đã giải quyết đúng. Khi so với nhân viên, nhóm tính thêm phần xử lý yêu cầu không thành công.

## 3. Giải pháp

Phần A–B gồm [bảng chi phí](bang_chi_phi.md), 9 kịch bản độ nhạy, giới hạn chạy lại 1–3 lần và trường hợp xem lại 100%. Phần C có [bảng phân loại lỗi](bang_loi.md) và 5 cách khắc phục. Phần D [chia ngẫu nhiên 20 nhân viên mỗi nhóm](pilot_plan.yaml), có đối chứng cùng thời điểm. Phần E xác định [chỉ số và sự kiện cần ghi](chi_so.md), sau đó tổng hợp thành [hồ sơ launch](ho_so_launch_v0.md). Số liệu được lưu trong [kết quả tính](ket_qua_tinh_toan.txt) và đối chiếu bằng [script csv/Decimal](../../src/kiem_so_doc_lap.py).

## 4. Kết quả

Chi phí mỗi việc thành công (CPS) là 4.471,97 đ; thời gian nhân viên chiếm 92,46% tổng chi phí [simulated]. Giới hạn 2 lần cho tổng hệ thống thấp nhất 6.901.220,23 đ [simulated], dù 1 lần cho CPS thấp nhất. Trong phạm vi noi_dia + hang_nang, hệ thống có cố định là 5.217,09 đ/yêu cầu ở đủ tải [simulated].

Xem lại 100% cho CPS 11.742,79–12.414,50 đ tùy phút làm lại, chưa có cố định/chuyển nhân viên [simulated]. Tỉ lệ đóng đúng hạn và không mở lại là 82,83%, sửa/bỏ gợi ý 27,12%, mở lại 4,25%. Đợt thử không có đối chứng nên chưa thể kết luận trợ lý làm tăng chất lượng. Hai bộ nhãn khớp 20/20; nguồn và quy trình ghi trong bảng C.

Pilot chấp nhận MDE +6 điểm: 5.980 mẫu thô/nhóm, DE 6,96, hiệu dụng 859,20; power 0,8010 ở +6 nhưng chỉ 0,6418 ở +5. Kế hoạch có bốn luật dừng, dự kiến chạy từ 01/12/2026 và quyết định ngày 05/01/2027. Nhóm đề xuất **Go có điều kiện**, chỉ phạm vi nội địa/hàng nặng; trước khi chạy cần kiểm tra an toàn, ghi đủ sự kiện và đo thời gian thực tế. [Phiếu tự chấm](phieu_cham.md): **98/100**, gồm 68/70 kỹ thuật và 30/30 Gate 2a. Phần C3 tự trừ 2 điểm do thiếu bản khóa riêng bộ nhãn 1 trước khi so.

## 5. Khó khăn và cách xử lý

Máy thiếu statsmodels nên nhóm cài thư viện trong `.venv`. Lỗi xuất tiếng Việt trên Windows được xử lý bằng UTF-8. Khi ghép bài, nhóm làm rõ 5.980 mẫu thô và 859 mẫu hiệu dụng, thống nhất cửa sổ theo dõi 7 ngày và bổ sung sự kiện để đo các ngưỡng dừng.

## 6. Tổng hợp đóng góp

| Thành viên | Phần đã bàn giao | Bằng chứng gốc |
| --- | --- | --- |
| Bình | A–B/E1, kiểm tra, tích hợp | `4bdce40`, `f3c48a4` |
| Long | Bảng chi phí, chỉ số/event, kiểm D1 | `19cb5be`, `093ec85` |
| Minh | C, code D1, kế hoạch pilot | `99aa565`, `60def4d` |
| Dũng | Khung launch, bộ nhãn 2, giữ hồ sơ | `fb2023d`, `0a72f5f` |

Công cụ và cách kiểm tra được ghi tại mục 5 của từng báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

16/16 kiểm tra đạt, kết quả kiểm số độc lập khớp với mô hình. Tuy vậy, thời gian xử lý là simulated, ICC và mức nền là giả định. Pilot cần đo thời gian thật, kiểm soát việc chia sẻ gợi ý giữa hai nhóm, có đủ 20 cụm mỗi nhánh và 299 yêu cầu/người. Kết quả là tự đánh giá hồ sơ; nhóm chưa có dữ liệu pilot thực tế.

## 8. Tài liệu tham khảo

[Quy tắc và công thức lab](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), đề bài `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, [rubric](../../RUBRIC.md). Không gọi model thật hoặc dùng API key trong bài tính.
