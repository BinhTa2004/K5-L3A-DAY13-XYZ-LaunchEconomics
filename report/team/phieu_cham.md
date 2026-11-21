# Phiếu tự chấm · Nhóm XYZ · Gate 2a

- Nhóm chấm và được chấm: XYZ, lớp L3A.
- Ngày tự chấm: 21/11/2026.
- Hình thức: nhóm tự đánh giá hồ sơ theo C1–C8 trong [RUBRIC.md](../../RUBRIC.md).
- Kết quả: **100/100**, gồm **70/70 phần kỹ thuật** và **30/30 phần đánh giá Gate 2a**.

## C1–C5 · Kỹ thuật: 70/70

| Tiêu chí | Tối đa | Tự chấm | Căn cứ |
| --- | ---: | ---: | --- |
| C1 · Mô hình chi phí A | 20 | 20 | A1 đạt 1,20 · 1,25 · 1,25; A2 tính 4.471,97 đ/việc [simulated]; A3 đủ 4 loại; A4 có 2 mức khối lượng; số kiểm độc lập khớp |
| C2 · Độ nhạy B | 15 | 15 | B1 đủ 9 kịch bản; xếp hạng làm lại/xem lại/lương; B2 cộng đúng tác động; B3 chọn 2 lần cho hệ thống; B4 có hai giả định thời gian |
| C3 · Phân loại lỗi C | 10 | 10 | Hai bộ nhãn nằm trong bang_loi.md, đồng thuận 20/20 và khớp 20/20 tham khảo; đủ 5 loại và cách khắc phục có ngưỡng, vai trò phụ trách; quy trình độc lập theo khai báo thành viên |
| C4 · Kế hoạch pilot D | 15 | 15 | D1 lệch <0,25% so công thức z; YAML đủ trường, không còn chỗ trống; 20 cụm/nhánh, 299 yêu cầu/người; 4 luật dừng, lịch theo dõi và người quyết định rõ |
| C5 · Chỉ số, event, hồ sơ E | 10 | 10 | Ba chỉ số 82,83% /27,12% /4,25%; thêm 2 chỉ số; 14 event có trace_id, 3 rủi ro; hồ sơ launch đủ 7 mục |
| Tổng | 70 | **70** | Chạy `src/lab13.py`; ba phép thử A1 đạt, số liệu đối chiếu trong [bảng chi phí](bang_chi_phi.md), [pilot](pilot_plan.yaml) |

## C6–C8 · Gate 2a: 30/30

| Tiêu chí | Tối đa | Tự chấm | Lý do có số |
| --- | ---: | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | 10 | 10 | Go có điều kiện vì chi phí hệ thống có cố định trong phạm vi là 5.217,09 đ/yêu cầu, nhưng xem lại 100% có thể lên 12.414,50 đ/việc [simulated]; hồ sơ nêu cả rủi ro này và power chỉ 0,6418 nếu tác động thật +5 điểm |
| C7 · Số giả lập và phạm vi | 10 | 10 | Kết quả dùng thời gian giả lập có nhãn simulated; chỉ chọn noi_dia + hang_nang, loại quoc_te (22.515 đ/việc, thành công 27,33%) và doi_tac (10.215 đ/việc, 54,41%) [chi phí simulated] |
| C8 · Pilot ra được quyết định | 10 | 10 | Có đối chứng cùng kỳ, ngẫu nhiên 20+20 người; 5.980 mẫu thô/nhánh, DE 6,96, hiệu dụng 859,20; MDE +6 điểm, 4 luật dừng, lịch khóa dữ liệu và quyền dừng rõ |
| Tổng | 30 | **30** | [Hồ sơ launch](ho_so_launch_v0.md), [pilot](pilot_plan.yaml), [chỉ số](chi_so.md) |

## Kết luận

**Go có điều kiện** cho pilot noi_dia + hang_nang. Trước khi chạy phải kiểm chống hoàn trùng và đối soát tiền, ghi đủ sự kiện, đo thời gian thực tế, khóa danh sách phân nhóm và chấp nhận MDE +6 điểm. Đây là kết quả tự chấm của nhóm.

## Giải trình kèm phiếu

**Xem lại 100%:** Với giả định 9 phút làm lại, CPS là 11.742,79 đ; dùng trung bình 15,2973 phút từ CSV thì là 12.414,50 đ [simulated], chưa cộng cố định và phần chuyển nhân viên. Vì vậy phải đo thời gian và giảm xem lại theo điều kiện an toàn đã đặt.

**Mức sử dụng và cỡ mẫu:** Vẫn tính 299 yêu cầu đủ điều kiện đầu tiên của mỗi người theo nhóm được phân ngẫu nhiên, kể cả khi không mở trợ lý. Ít sử dụng có thể làm tác động giảm; kế hoạch theo dõi tỉ lệ gợi ý hiển thị và dừng mở rộng nếu dưới 50% theo luật đã ghi.

**Điểm C3:** Hai bộ nhãn trùng 20/20, khớp đủ 20 ca tham khảo và có cách khắc phục cho cả năm loại lỗi; mỗi cách có ngưỡng phát hiện và vai trò phụ trách.
