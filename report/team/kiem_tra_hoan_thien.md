# Rà soát hoàn thiện · Nhóm XYZ · Lab 13

Bảng tự kiểm dựa trên phân công, rubric, commit bàn giao và kết quả chạy chương trình. Nhóm đã tự chấm 98/100: phần kỹ thuật 68/70, Gate 2a 30/30; chi tiết tại [phiếu tự chấm](phieu_cham.md).

## Kết quả theo từng người

| Thành viên | Phần đã có khi rà soát | Phần đã hoàn thiện thêm | Trạng thái còn lại |
| --- | --- | --- | --- |
| Bình | A–B/E1, 12 kiểm tra, tích hợp nhánh | Tính power ở +5/+6; so chi phí cùng mẫu số gồm nhân viên và cố định; thêm 4 kiểm tra và script csv/Decimal; cập nhật TEAM/báo cáo | Code chạy đủ A–B–D1–E1; 16 kiểm tra đạt |
| Long | Bảng chi phí, 3 chỉ số, 9 event, 3 rủi ro; kiểm D1 | Schema 14 event có thời gian/khóa, nối với luật dừng/CPS; B4 dùng số chính xác; báo cáo tự đánh giá từ bằng chứng | Phần số và đặc tả hoàn thiện; phút thật/event thật phải đo khi pilot |
| Minh | C với 2 cột nhãn khớp, code D1/YAML | Rõ 5.980 thô/859 hiệu dụng, power +5 chỉ 0,6418; lịch đủ 7 ngày theo dõi; 4 luật dừng đo được; sửa tên event đồng nhất | Bảng C giữ nguyên nhãn; tính độc lập/thời điểm theo khai báo, chưa có file khóa riêng bộ 1 để kiểm lại lịch sử |
| Dũng | Khung launch và bản nhãn 2 | Điền đủ 7 mục launch/đề xuất có điều kiện, viết báo cáo nhóm và báo cáo cá nhân, hoàn thiện phiếu tự chấm theo rubric | Đã có điểm, căn cứ và giải trình trong phiếu |

Bản tích hợp `86f7d53` bổ sung các mục trong cột thứ ba. Phạm vi dùng công cụ được ghi trong báo cáo cá nhân. CSV, bản khởi đầu, file mẫu và nhãn gốc của Dũng được giữ nguyên.

## Đối chiếu rubric

| Tiêu chí | Bằng chứng và kết quả tự kiểm | Giới hạn |
| --- | --- | --- |
| C1 · A | A1=1,20/1,25/1,25; A2/A3/A4 khớp, nhãn simulated có ở chi phí | Giá/thời gian là giả định lab |
| C2 · B | B1 đủ 9; B2 xếp làm lại/xem lại/lương; B3 giới hạn 2 rẻ nhất; B4 hai giả định | Không dùng CPS làm số so sánh hệ thống nếu chưa cùng mẫu số |
| C3 · C | Hai cột hiện trùng 20/20, khớp 20/20 với nhãn tham khảo, 5 loại có khắc phục đo được và owner | Đối chiếu tham khảo chỉ ở bước rà soát; không xác nhận ngược quy trình độc lập chỉ bằng 100% |
| C4 · D | D1 đối chiếu công thức z, YAML đọc được, 20 cụm/nhóm, 299 yêu cầu/người, 4 luật dừng, lịch/rollback | ICC=0,02 và lịch 01/12/2026–05/01/2027 là đề xuất giả định; chưa có roster thật hoặc ký duyệt |
| C5 · E | Ba chỉ số đúng; thêm 2 chỉ số, 14 event và 3 rủi ro; launch đủ 7 mục | Schema chưa được triển khai trong hệ thống thật |
| C6–C8 · Tự chấm Gate 2a | 10+10+10=30/30; đề xuất có căn cứ, nhãn simulated và phạm vi rõ, đủ mẫu và luật dừng | Kết quả tự đánh giá của nhóm |

## Bằng chứng chạy lại

- [Output code](ket_qua_tinh_toan.txt): A1–A4, B1–B4, D1/power và E1; không nhập tay số vào artifact này.
- [Kiểm độc lập](kiem_so_doc_lap.json): csv/Decimal kiểm A/E và NormalDist kiểm D1, không import `lab13`; token/tool/tổng/CPS khớp sai số <0,000001 đ.
- `src/test_lab13.py`: 16 kiểm tra đạt; gồm chọn mẫu theo phạm vi, run lỗi mất tiền, retry không sửa đầu vào, đếm review theo request, mẫu số chỉ số, D1/power/lịch và chi phí đầy đủ.
- `pilot_plan.yaml`: đọc được bằng `yaml.safe_load`, không còn dấu hỏi ngoài chú thích; 4 luật đủ NẾU/TRONG/THÌ/KHÔNG THÌ; 20×299=5.980 và 5.980/6,96=859,1954.
- Công thức z D1 cho 1.251/3.103, statsmodels cho 1.250/3.100: sai khác <0,25%, trong ngưỡng 2% của rubric.

## Kết luận rà soát

1. Code, sáu hồ sơ nhóm, bốn báo cáo cá nhân và phiếu tự chấm đã đủ. Phần kỹ thuật tự chấm 68/70, Gate 2a 30/30, tổng 98/100.
2. C3 tự trừ 2 điểm vì chưa có bản khóa riêng của bộ nhãn 1 trước khi so. Nguồn và hạn chế bằng chứng đã ghi trong bảng C; giữ nguyên dữ liệu nhãn hiện có.
3. Trước pilot: roster 40 người/12 depot, chống hoàn trùng/đối soát, log và phút đo thật, chữ ký chấp nhận MDE. Đây là điều kiện trong kế hoạch, không phải thiếu code bắt buộc của lab.
4. Mỗi người tự nộp link trên LMS và kiểm tra quyền truy cập repo của người chấm. Trạng thái nộp LMS chưa được cập nhật.
