# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (hàm `tinh_chi_so`, commit `4bdce40`). Long kiểm lại bằng script riêng, kết quả khớp. Toàn bộ dữ liệu là giả lập.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu ở nhóm can thiệp mà nhân viên mở bằng trợ lý | Số `refund_request_created` (arm = can_thiep) có ít nhất một `agent_suggestion_shown` cùng `trace_id`, chia số `refund_request_created` (arm = can_thiep) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền khi kiểm tra mẫu hằng tuần | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số `audit_sample_checked`. Chỉ số này bắt cả lỗi ngầm mà khách chưa mở lại | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83% (chính), 27,12% (dùng) và 4,25% (an toàn). Đợt chạy thử không có nhóm đối chứng, nên các số này không chứng minh trợ lý đã nâng chỉ số so với mức 0,70.

## Danh sách event

Chín event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, depot, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi nhân viên làm lại xong |
| `handoff_to_staff` | Agent | ly_do, so_lan_da_chay, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, ly_do, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, trên mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số, có `created_at`) + `ticket_closed` (đóng trong 24 giờ) + `ticket_reopened` (không mở lại trong 7 ngày).
- Dùng (bỏ qua gợi ý): `staff_review_decision` (tử số: sua hoặc bo; mẫu số: mọi quyết định).
- An toàn (lỗi lọt đến khách): `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown`, chia `refund_request_created` có arm = can_thiep.
- An toàn (tự đề xuất): `audit_sample_checked`.
- Chi phí mỗi việc thành công trong pilot: `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho cột simulated).

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy trong `bang_chi_phi.md`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,77%, từ 4.472 đ lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần trong phạm vi > 7% (đợt chạy thử: 4,89%, tức 48/982) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.414 đ = 1,03× nếu làm lại mất 15,3 phút như trong dữ liệu [simulated] | % yêu cầu được xem lại > 50% sau 2 tuần pilot, hoặc phút xem lại đo thật > 5,1 phút/lần | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, đàm phán lại chi phí cố định | PM trợ lý hoàn phí |
