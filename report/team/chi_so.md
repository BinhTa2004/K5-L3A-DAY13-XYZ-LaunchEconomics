# Đặc tả chỉ số, event và rủi ro kinh tế · E1, E2

Số cơ sở từ `src/lab13.py` của Bình (`4bdce40`), Long kiểm ở `19cb5be` và `093ec85`; lần tích hợp cuối bổ sung schema để các gate C–D đo được. Toàn bộ dữ liệu là giả lập; thời gian và kết quả chi phí dẫn từ cột `_simulated` có nhãn simulated.

## E1 · Chỉ số

| Loại | Chỉ số | Công thức | Kết quả trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính | Đóng 24 giờ, không mở lại 7 ngày | Yêu cầu `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0` / tổng yêu cầu | 994/1.200 = 82,83% |
| Dùng | Bỏ qua gợi ý | Yêu cầu được xem lại có quyết định `sua` hoặc `bo` / số được xem lại | 48/177 = 27,12% |
| An toàn | Mở lại trong 7 ngày, đại diện lỗi lọt tới khách | Yêu cầu `mo_lai_trong_7_ngay=1` / tổng yêu cầu | 51/1.200 = 4,25% |
| Dùng, bổ sung | Tỉ lệ yêu cầu can thiệp có gợi ý hiển thị | Yêu cầu arm=can_thiep có `agent_suggestion_shown` / mọi yêu cầu đủ điều kiện arm=can_thiep | Chưa đo trong CSV; đặc tả cho pilot |
| An toàn, bổ sung | Sai tiền qua kiểm toán mẫu | Đơn audit có tiền hoàn khác tiền đúng / đơn audit; lấy một bản chốt mỗi đơn | Chưa đo trong CSV; bắt cả lỗi ngầm |

Trong phạm vi noi_dia + hang_nang: chính 906/982 = 92,26%; sửa/bỏ 27/128 = 21,09%; mở lại 39/982 = 3,97%. Riêng hang_nang mở lại 13/158 = 8,23%, cần xem lại và báo riêng, không áp ngưỡng toàn phạm vi trực tiếp cho loại này.

Đợt chạy thử không có đối chứng. Không coi 82,83% so với baseline giả định 70% là tác động nhân quả. Trong pilot, đo intention-to-treat trên 20 staff mỗi nhánh và cohort cố định trong `pilot_plan.yaml`; phải đủ 7 ngày theo dõi trước khi chốt kết quả.

## Danh sách event

14 event. Mỗi event có `event_id`, `occurred_at` và `trace_id`; event cấp yêu cầu còn có `request_id`, `staff_id`, `arm`, `depot`, `loai`. `pilot_staff_assigned` dùng trace của phiên phân nhóm, nối qua `staff_id` với trace yêu cầu. Đây là schema đề xuất, chưa phải hệ thống log đã triển khai.

| Event | Ai tạo | Thuộc tính riêng ngoài trường chung | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `created_at`, `order_id`, `so_tien`, `eligible` | Khi yêu cầu tới, cả hai nhánh |
| `agent_run_completed` | Agent | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` | Mọi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện staff | `suggestion_id`, `so_tien_de_xuat` | Khi gợi ý thật sự hiển thị |
| `staff_review_decision` | Giao diện staff | `decision_id`, `suggestion_id`, `quyet_dinh`, `phut_xem_lai`, `final` | Khi giữ/sửa/bỏ; phút đo thật |
| `staff_rework_completed` | Hệ thống CSKH | `work_id`, `phut_lam_lai`, `ly_do` | Khi làm lại xong; phút đo thật |
| `handoff_to_staff` | Agent | `ly_do`, `so_lan_da_chay` | Chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `resolution_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `reopened_at`, `ly_do` | Khi mở lại |
| `audit_sample_checked` | Kế toán | `audit_id`, `order_id`, `so_tien_da_hoan`, `so_tien_dung`, `policy_version` | Kiểm ngẫu nhiên hằng tuần |
| `refund_ledger_write` | Sổ cái | `ledger_entry_id`, `order_id`, `idempotency_key`, `so_tien`, `expected_amount`, `status`, `policy_version` | Mỗi lần ghi/chặn lệnh tiền, gồm lỗi |
| `request_outcome_finalized` | Bộ đối soát | `ket_qua`, `closed_at`, `followup_complete`, `amount_correct`, `finalized_at` | Khi đủ cửa sổ theo dõi và đối soát tiền |
| `out_of_scope_query` | Bộ phân loại | `reason`, `handoff_required` | Phát hiện ngoài phạm vi |
| `bank_payout_failed` | Thanh toán | `order_id`, `error_code` | Chuyển tiền bị từ chối |
| `pilot_staff_assigned` | Điều phối pilot | `staff_id`, `arm`, `depot`, `seed`, `assigned_at`, `rollout_enabled_at` | Khóa roster và bật quyền theo lịch |

## Cách tính từ event và gate

| Chỉ số/gate | Event và quy tắc |
| --- | --- |
| Chính | Nối `refund_request_created.created_at`, `ticket_closed.closed_at`, `ticket_reopened.reopened_at` theo request; lấy yêu cầu đủ điều kiện, đóng <=24h và không mở lại <=7 ngày |
| Bỏ qua gợi ý | `staff_review_decision`: một quyết định cuối mỗi yêu cầu được xem lại; tử số `sua`/`bo`, mẫu số gồm cả `giu`; không đếm mỗi lần bấm |
| Mở lại | Đếm request có `ticket_reopened` trong 7 ngày, chia cohort request đủ theo dõi; không đếm số event mở lại |
| Sử dụng | Request can thiệp có ít nhất một `agent_suggestion_shown` / request can thiệp đủ điều kiện; cùng công thức với luật dừng <50% |
| Audit sai tiền | Một kết quả audit chốt mỗi đơn; `so_tien_da_hoan != so_tien_dung`; bổ sung lý do để bắt hoàn thừa như ca 5 |
| CPS trong pilot | Token/tool trên mọi run + phút review/rework đo thật; chia số `request_outcome_finalized.ket_qua=thanh_cong`, theo định nghĩa đóng/không mở lại/đúng tiền của lab |
| Chi phí cả hệ thống | Theo B3: tổng trợ lý +12.000 đ mỗi yêu cầu không thành công, chia tổng yêu cầu; cộng 40 triệu/tháng phân bổ theo khối lượng thực tế khi báo phần có cố định [giả định lab, simulated nếu dùng phút giả lập] |
| Hoàn trùng | Từ `refund_ledger_write`: cùng `order_id` có >=2 bút toán hoàn thành công trong 24h; bút toán retry bị chặn không tính trùng; >=1 ca thì dừng ngay |
| Ngoài phạm vi chưa chuyển | `out_of_scope_query` không có `handoff_to_staff` cùng request; tên event thống nhất với bảng C |
| Đủ mẫu | `pilot_staff_assigned` khóa 20+20 người; chọn 299 request đầu đủ điều kiện mỗi staff trong kỳ, kể cả không dùng trợ lý; theo dõi đến ngày khóa dữ liệu |

Dedupe theo `event_id`, rồi theo khóa nghiệp vụ của từng chỉ số; nối nhiều run với một request không được nhân số yêu cầu. Bản chốt muộn và audit phải có phiên bản, lưu lịch sử. Dùng phút đo thật từ tuần 1, không coi cột simulated là thời gian quan sát; đo riêng phần nhân viên xử lý sau handoff để tránh cộng một khoảng thời gian hai lần.

## E2 · Rủi ro kinh tế

Số lấy từ [bảng chi phí](bang_chi_phi.md); mọi tác động tiền trong bảng này là simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại gấp đôi | CPS +51,77%, lên 6.786,90 đ [simulated] | Làm lại >7%/tuần; nền phạm vi 48/982=4,89% | Rà 20 trace, thu hẹp về noi_dia nếu gate vượt | PM trợ lý hoàn phí |
| Xem lại 100% kéo dài | CPS 11.742,79 đ với 9 phút làm lại; 12.414,50 đ với 15,2973 phút [simulated] | Xem lại >50% sau 2 tuần; phút review vượt hòa vốn 5,12 hoặc 4,80 [simulated] | Chỉ giảm review theo gate audit và sửa/bỏ đã ký; không hạ an toàn để đạt chi phí | Trưởng nhóm CSKH |
| Khối lượng giảm | Cố định/việc tăng 1.185,19 ->2.370,37 đ khi 45.000 ->22.500 yêu cầu/tháng [simulated] | Thành công/tuần <50% kế hoạch | Dừng mở rộng, xem lại hợp đồng cố định | PM trợ lý hoàn phí |

Ngưỡng chi phí và hành động có quyền dừng xem [pilot_plan.yaml](pilot_plan.yaml); danh sách trên là đặc tả cần bật trước pilot, không chứng minh các cảnh báo đã hoạt động.
