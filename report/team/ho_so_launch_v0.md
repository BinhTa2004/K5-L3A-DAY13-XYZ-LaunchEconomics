# Hồ sơ launch v0 · LogiX-VN · Gate 2a

Nhóm XYZ · L3A · Người giữ hồ sơ: Dũng. Dữ liệu lab giả lập; nguồn: [chi phí](bang_chi_phi.md), [chỉ số](chi_so.md), [lỗi](bang_loi.md), [pilot](pilot_plan.yaml).

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.471,97 đ; phạm vi noi_dia + hang_nang 3.413,90 đ chưa cố định, 4.599,09 đ có cố định ở 45.000 yêu cầu/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại +51,77%; xem lại +40,70%; lương +23,12% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống + cố định trong phạm vi: 5.217,09 đ/yêu cầu ở đủ tải; 6.303,31 đ ở nửa tải, so 12.000 đ thủ công [simulated] | Giả lập | Trưởng bộ phận Vận hành CSKH |
| 4 · Chỉ số | Toàn mẫu: chính 82,83%; sửa/bỏ 27,12%; mở lại 4,25%. Phạm vi mở lại 3,97%, riêng hang_nang 8,23%; 14 event đã đặc tả, chưa triển khai | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Lỗi và khắc phục | Hai cột nhãn khớp 20/20=100%; 5 loại lỗi có cách phát hiện và vai trò phụ trách; nguồn và quy trình ghi trong bảng C | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot | 20+20 nhân viên; MDE +6 điểm; 5.980 mẫu thô/nhóm =299/người, DE 6,96, hiệu dụng 859,20; power chỉ 0,6418 nếu thật sự +5; 4 luật dừng, quyết định đề xuất 05/01/2027 | Xong, có bằng chứng | Trưởng bộ phận Vận hành CSKH |
| 7 · Rủi ro kinh tế | Xem lại 100%: 11.742,79 đ/việc với 9 phút làm lại; 12.414,50 đ với 15,2973 phút; chưa cố định/chuyển nhân viên [simulated] | Giả lập | PM trợ lý hoàn phí |

Điều kiện trước khi chạy pilot; lịch 01/12/2026–05/01/2027 là đề xuất giả định, chưa có phê duyệt:

- Kỹ sư trưởng agent: trước 01/12/2026 kiểm chống hoàn trùng, đối soát sổ cái và đủ event; trước 07/12 thay phút simulated bằng đo thật.
- Trưởng bộ phận Vận hành CSKH: trước 01/12 ký chấp nhận MDE +6, power khi tác động chỉ +5 và danh sách 20+20 người; chỉ lấy mẫu 15–28/12, theo dõi đến 04/01.
- Trưởng nhóm CSKH: trước 08/12 đánh giá xem lại 100% hang_nang; chỉ giảm khi đạt gate audit và sửa/bỏ, không hạ an toàn để đạt chi phí.
- PM trợ lý hoàn phí: kiểm chi phí hằng tuần; không mở rộng nếu vượt gate hoặc thiếu mẫu. Đến 05/01 thiếu 299 yêu cầu/người thì No-go cho mở rộng vì chưa đủ bằng chứng.

Phạm vi chỉ noi_dia + hang_nang; loại quoc_te (22.515 đ/việc, 27,33% thành công) và doi_tac (10.215 đ/việc, 54,41%) [chi phí simulated]. Nhóm tự chấm Gate 2a 30/30; tổng C1–C8 là 98/100, xem [phiếu chấm](phieu_cham.md).

**Đề xuất: Go có điều kiện.**
