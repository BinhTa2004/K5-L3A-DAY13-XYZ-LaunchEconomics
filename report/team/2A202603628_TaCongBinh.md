# Báo cáo cá nhân — Tạ Công Bình — 2A202603628

Trạng thái: đã triển khai A–B và phép tính ba chỉ số E1 với ChatGPT/Codex hỗ trợ; code chạy được, 12 bài kiểm tra tự động đạt. Long chưa xác nhận kiểm độc lập; D1 do Minh bổ sung. Phân công: [TEAM.md](../../TEAM.md).

## 1. Thông tin thành viên

- Họ tên: Tạ Công Bình
- MSSV: 2A202603628
- GitHub: BinhTa2004
- Vai trong nhóm: Người viết code A–B, hỗ trợ tính E; trưởng nhóm, tích hợp và nộp repo.

## 2. Phần việc được giao

- Viết A1–A4 và B1–B4 trong `src/lab13.py`, chạy ba phép thử A1 và in các bảng.
- Bàn giao code A–B cho Minh viết D1; sau khi tích hợp D1, thêm phép tính ba chỉ số E và gửi output cho Long.
- Kiểm tra gói nộp, tích hợp pull request và push; cập nhật bằng chứng đóng góp trong `TEAM.md`.

## 3. Đóng góp cụ thể đã thực hiện

- Hoàn thiện ba hàm A1, mô hình A2 cộng mọi run kể cả lỗi và chỉ chia cho yêu cầu thành công; tự lọc runs theo `request_id`, không sửa DataFrame đầu vào.
- In bảng bốn loại A3, tỉ lệ run `ok` theo lần thử và A4 với cố định 40 triệu đ/tháng ở hai mức khối lượng.
- Hoàn thiện chín kịch bản B1, kịch bản cặp và xếp hạng B2, chi phí cả hệ thống theo giới hạn chạy B3, xem lại 100% B4 ở hai giả định thời gian làm lại.
- Thêm ba chỉ số E1 có tử số/mẫu số rõ ràng; thêm xử lý đầu ra UTF-8 trên Windows và đọc CSV theo vị trí code.
- Bổ sung `src/test_lab13.py` với ca tính tay độc lập để kiểm chạy lỗi vẫn mất tiền, lọc đúng phạm vi, không đếm trùng lượt xem lại, không sửa dữ liệu đầu vào và không dùng sai mẫu số.
- Phần tính E1 được làm sớm để Long có số kiểm. Giữ vị trí `TODO CP4` cho Minh tích hợp D1; chưa ghi nhận việc Long kiểm số hoặc hội đồng duyệt bài khi chưa diễn ra.

## 4. Bằng chứng

Code: [lab13.py](../../src/lab13.py). Kiểm tra: [test_lab13.py](../../src/test_lab13.py). Cách chạy/bàn giao: [src/README.md](../../src/README.md).

Các lệnh đã chạy trong `src/`, bằng Python 3.12.9 và pandas 2.2.3:

```powershell
python lab13.py
python -m unittest -v test_lab13
```

Chương trình chạy hết phần A–B/E1, ba phép thử A1 đạt 1,20 · 1,25 · 1,25; 12/12 bài kiểm tra đạt. Đối chiếu số tiền làm tròn trong hướng dẫn ở sai số tối đa 0,5 đ (dòng B4 dùng phút trung bình chính xác kiểm riêng), chặt hơn mức 2% của lab.

| Kết quả từ CSV | Giá trị | Nhãn |
| --- | --- | --- |
| A2: tổng chi phí / số thành công | 4.373.585,13 đ / 978 = 4.471,97 đ/việc | simulated |
| A2: chi phí cả hệ thống / tổng yêu cầu | 7.037.585,13 đ / 1.200 = 5.864,65 đ/yêu cầu; chưa có cố định | simulated |
| A4: CPS có cố định, 45.000 và 22.500 yêu cầu/tháng | 4.599,09 và 5.784,27 đ/việc trong phạm vi | simulated |
| B2: token và xem lại cùng gấp đôi | 6.543,12 đ/việc; tăng 46,31% | simulated |
| B3: giới hạn 2 lần cho chi phí hệ thống thấp nhất | 6.901.220,23 đ; giới hạn 1 lần cho CPS thấp nhất | simulated |
| B4: xem lại 100%, làm lại 9 phút | 11.742,79 đ/việc; hòa vốn xem lại 5,12 phút | simulated |
| B4: làm lại trung bình 15,2973 phút từ CSV | 12.414,50 đ/việc; hòa vốn xem lại 4,80 phút | simulated |
| E1: đóng 24h, không mở lại 7 ngày | 994/1.200 = 82,83% | dữ liệu lab giả lập |
| E1: sửa/bỏ trong số được xem lại | 48/177 = 27,12% | dữ liệu lab giả lập |
| E1: mở lại trong 7 ngày | 51/1.200 = 4,25% | dữ liệu lab giả lập |

B1 xếp hạng ảnh hưởng: làm lại (+51,77%), xem lại (+40,70%), lương (+23,12%) [simulated]. Bảng chi phí và đặc tả chỉ số do Long kiểm và tổng hợp theo phân công, không dùng báo cáo này để thay lượt kiểm của Long.

## 5. Công cụ AI đã dùng

ChatGPT/Codex hỗ trợ đọc yêu cầu, viết code A–B/E1, viết kiểm tra, chạy lệnh và cập nhật báo cáo này theo yêu cầu của Bình. Nội dung có hỗ trợ AI; không khai là toàn bộ do thành viên tự viết thủ công.

Kiểm chứng trong phiên hỗ trợ: dùng ví dụ nhỏ tính tay, đối chiếu số liệu hướng dẫn với output từ CSV, kiểm tính tuyến tính của độ nhạy và sự khác nhau giữa hai mục tiêu chi phí. Công thức tham khảo từ `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Không dùng API, không sửa CSV, không tạo nhãn độc lập hoặc kết quả duyệt chéo thay các thành viên.

## 6. Tự đánh giá

Phần code được giao đã có kết quả tái lập trên dữ liệu lab. Giờ nhân viên chiếm 92,46% tổng chi phí [simulated]; xem lại 100% có thể đắt hơn nhân viên tự làm nếu thời gian làm lại gần dữ liệu, nên kết luận phải nêu rõ giả định.

D1, các lượt kiểm độc lập và kết quả pilot chưa có bằng chứng trong phần việc này. Bình cần tự đọc lại code, chạy lại và giải thích được tử số/mẫu số, quy ước chi phí hệ thống và phạm vi phân bổ cố định trước khi bảo vệ bài.
