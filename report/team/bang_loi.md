# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Khuất Tiến Minh (2A202603616) · Người gắn nhãn 2: Nguyễn Tuấn Dũng (2A202603608, bản nhãn bàn giao ở commit `0a72f5f`, chép nguyên văn ở cuối file này) (gắn độc lập trong 8 phút, không trao đổi, giữ nguyên bộ nhãn gốc sau khi so)

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

Nguồn: bộ nhãn 2 của Dũng, commit `0a72f5f`, lưu nguyên văn ở cuối file; bộ nhãn 1 và bảng so của Minh, commit `99aa565`. Hai cột khớp 20/20. Quy trình gắn độc lập theo khai báo của hai thành viên. Đề yêu cầu hai bộ nhãn trong bảng này, không yêu cầu tạo file khóa nhãn riêng.

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
| 20 | Hệ thống | Từ `refund_ledger_write`: cùng `order_id` có ≥2 bút toán hoàn thành công trong 24 giờ; ≥1 ca thì cảnh báo tức thời, không đếm retry bị chặn. | Bắt buộc khoá chống trùng theo nghiệp vụ ở API hoàn tiền và chặn lệnh thứ hai khi đang xử lý; đối soát trước khi mở lại. | Kỹ sư backend hệ thống thanh toán (Backend Engineer) |
| 18 | Ngữ cảnh | Event `ticket_reopened` với lý do "thiếu tiền hoàn" trên đơn tính đúng chính sách vượt 2% tổng đơn hoàn mỗi tuần, rà soát hằng tuần. | Hiển thị rõ công thức tính tiền hoàn trong tin nhắn (phí gốc × tỉ lệ hoàn = số tiền nhận) và dẫn điều khoản áp dụng. | Quản lý sản phẩm CSKH (Product Manager) |
| 13 | Giới hạn hệ thống | `out_of_scope_query` không kèm `handoff_to_staff` cùng request vượt 0,5% lượt hội thoại mỗi tuần. | Phân loại phạm vi từ đầu: từ chối lịch sự, giải thích giới hạn và chuyển kênh bảo hiểm đối tác. | Kỹ sư AI phụ trách trợ lý (AI Engineer) |
| 5 | Ngầm | `audit_sample_checked` trên mẫu 5% đơn có mã giảm giá mỗi tuần: tiền hoàn >tiền đúng ở ≥1% mẫu; ≥1 ca xác nhận sai tiền kích hoạt gate D. | Tính theo `net_paid_amount` sau giảm; đối soát cuối ngày và rà lại mọi đơn cùng phiên bản công thức lỗi. | Trưởng nhóm vận hành đối soát tài chính (Finance Ops Lead) |

## Bản nhãn 2 đã bàn giao

Nội dung từ commit `0a72f5f`, giữ nguyên nhãn và lý do khi chuyển vào file nhiệm vụ C:

### Bộ nhãn 2 · Nguyễn Tuấn Dũng · 20 ca lỗi (bản gốc, không sửa sau khi so)

Gắn trước khi xem nhãn của Minh hoặc nhãn tham khảo. Bản nháp do Claude gắn từ mô tả ca và định nghĩa năm loại trong đề bài; Dũng soát lại trước khi khóa. Minh chép nguyên bộ này vào `bang_loi.md`.

| Ca | Nhãn | Lý do ngắn |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu số tài khoản |
| 2 | Hệ thống | Gọi tool sai tham số, hoàn thiếu |
| 3 | Ngữ cảnh | Đúng thiết kế (ví LogiX), khách kỳ vọng về ngân hàng |
| 4 | Giới hạn hệ thống | Không có dữ liệu chặng hãng ngoài |
| 5 | Ngầm | Hoàn thừa 12.000 đ, không ai nhận ra |
| 6 | Do người dùng | Khách chọn sai mục |
| 7 | Hệ thống | Sổ cái lỗi 503 nhưng vẫn báo "đã hoàn" |
| 8 | Hệ thống | Dẫn điều khoản không tồn tại |
| 9 | Do người dùng | Nhập mã đơn sàn thay vì mã vận đơn |
| 10 | Ngữ cảnh | Đúng chính sách, nhưng app vẫn hiện "cam kết 24 giờ" |
| 11 | Giới hạn hệ thống | Không xử lý được âm thanh |
| 12 | Ngầm | Token D05 gấp 3 lần suốt 3 tuần, không ai thấy |
| 13 | Giới hạn hệ thống | Ngoài phạm vi (bảo hiểm) |
| 14 | Do người dùng | Khách bấm nhầm xác nhận |
| 15 | Hệ thống | Tính 100% thay vì 50% |
| 16 | Ngữ cảnh | Gửi lúc 2:14 sáng đúng thiết kế, khách thấy phiền |
| 17 | Ngầm | Bảng giá cũ trong bộ nhớ đệm, 212 đơn, không ai mở lại |
| 18 | Ngữ cảnh | Tính đúng, nhưng tin nhắn thiếu cách tính |
| 19 | Giới hạn hệ thống | Chỉ truy cập được dữ liệu 12 tháng |
| 20 | Hệ thống | Thiếu khoá chống trùng, hoàn hai lần |

Ca dễ lệch: 13 (Giới hạn hệ thống hay Hệ thống), 9 (Do người dùng hay Giới hạn hệ thống), 7 và 8 (Hệ thống hay Ngầm).
