# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Khuất Tiến Minh (2A202603616) · Người gắn nhãn 2: Nguyễn Tuấn Dũng (2A202603608, bản gốc lưu tại `report/team/nhan_dung_doc_lap.md`, commit `0a72f5f`) (gắn độc lập trong 8 phút, không trao đổi, giữ nguyên bộ nhãn gốc sau khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (đạt ngưỡng ≥ 80%, không cần viết lại định nghĩa).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không phát sinh ca không trùng (20/20 trùng giữa hai bộ nhãn độc lập).
- Quy tắc ranh giới nhóm thống nhất thêm cho các ca dễ nhầm khi đối chiếu nguyên nhân gốc:
  - **Ca 13 (Giới hạn hệ thống vs Hệ thống):** gắn **Giới hạn hệ thống** vì nguyên nhân gốc là yêu cầu bảo hiểm nằm ngoài phạm vi trợ lý, không gắn theo chỗ cần sửa (cách trả lời chung chung).
  - **Ca 9 (Do người dùng vs Giới hạn hệ thống):** gắn **Do người dùng** vì nguyên nhân gốc là khách nhập sai loại mã (mã đơn sàn thương mại điện tử thay vì mã vận đơn).
  - **Ca 7 và Ca 8 (Hệ thống vs Ngầm):** gắn **Hệ thống** vì trợ lý báo sai kết quả khi API lỗi 503 (Ca 7) hoặc bịa điều khoản không tồn tại (Ca 8), vi phạm trực tiếp thiết kế và chính sách thay vì lỗi âm thầm không ai nhận ra như Ca 5, 12, 17.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_payout_failed` (mã lỗi định dạng tài khoản) vượt 1% tổng lệnh hoàn trong ngày, kiểm tra hằng ngày. | Thêm kiểm tra độ dài và định dạng số tài khoản ngay trên form trước khi gửi lệnh hoàn; báo lỗi cụ thể để khách sửa. | Kỹ sư giao diện CSKH (Frontend Engineer) |
| 20 | Hệ thống | Event `duplicate_refund_detected` (trùng `order_id` có ≥ 2 lệnh hoàn trong 24 giờ) > 0 ca, cảnh báo tức thời. | Bắt buộc dùng khoá chống trùng (`idempotency_key` theo `order_id`) ở API hoàn tiền và chặn gửi lệnh thứ hai khi đơn đang xử lý. | Kỹ sư backend hệ thống thanh toán (Backend Engineer) |
| 18 | Ngữ cảnh | Event `ticket_reopened` với lý do "thiếu tiền hoàn" trên đơn tính đúng chính sách vượt 2% tổng đơn hoàn mỗi tuần, rà soát hằng tuần. | Hiển thị rõ công thức tính tiền hoàn trong tin nhắn (phí gốc × tỉ lệ hoàn = số tiền nhận) và dẫn điều khoản áp dụng. | Quản lý sản phẩm CSKH (Product Manager) |
| 13 | Giới hạn hệ thống | Event `out_of_scope_query` (từ khóa "bảo hiểm" / sản phẩm đối tác) không kèm `handoff_triggered` vượt 0,5% lượt hội thoại mỗi tuần. | Bổ sung bộ phân loại phạm vi ngay đầu luồng: từ chối lịch sự, nêu rõ ngoài phạm vi trợ lý và chuyển ngay sang kênh bảo hiểm đối tác. | Kỹ sư AI phụ trách trợ lý (AI Engineer) |
| 5 | Ngầm | Event `audit_refund_overpaid` từ kiểm toán mẫu 5% đơn có mã giảm giá hằng tuần: chênh lệch > 0 đ xuất hiện ở ≥ 1% mẫu kiểm. | Khóa công thức tính hoàn tiền theo trường `net_paid_amount` (giá sau giảm) thay vì giá gốc và chạy đối soát tự động cuối ngày. | Trưởng nhóm vận hành đối soát tài chính (Finance Ops Lead) |
