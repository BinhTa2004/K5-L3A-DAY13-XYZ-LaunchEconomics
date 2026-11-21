# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

Nguồn số: output `python lab13.py` trên nhánh `main` (commit `4bdce40`), Long điền và kiểm. Chưa cộng chi phí cố định, trừ bảng A4.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

`lab13.py` in "Ba phép thử đáp án biết trước: ĐẠT".

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần** hoá đơn chia số yêu cầu (4.472 / 274,65) [simulated].
- Khoản lớn nhất là làm lại, chiếm **51,77%** tổng chi phí [simulated]. Giờ nhân viên (xem lại + làm lại) chiếm 92,46% [simulated].
- So với nhân viên tự làm: (4.373.585 + 222 ca không thành công × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated].

### Kiểm số độc lập (Long)

Script riêng chỉ dùng pandas và công thức trong `docs/du_lieu_va_cong_thuc.md`, không gọi `lab13.py`:

- Token = 5.771.712 / 1.000 × 26 + 734.774 / 1.000 × 130 = 150.064,51 + 95.520,62 = **245.585,13 đ**.
- Tool = 5.600 lần × 15 = **84.000 đ**. Xem lại = 890 phút × 2.000 = **1.780.000 đ** [simulated]. Làm lại = 1.132 phút × 2.000 = **2.264.000 đ** [simulated].
- Chi phí mỗi việc thành công = 4.373.585,13 / 978 = **4.471,97 đ** [simulated]. Dòng quoc_te ở A3 = 22.515,17 đ [simulated]. Cả hai lệch 0% so với output của Bình.

## A3 · Tách theo loại yêu cầu

Chi phí ở bảng này là simulated, chưa có chi phí cố định.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.215 đ [simulated] | 0,85× |

- **quoc_te không đáng** để trợ lý xử lý: 1,88× của 12.000 đ [simulated], chỉ 27,33% thành công. doi_tac sát ngưỡng (0,85× [simulated]) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot.
- Chạy lại không giúp quoc_te: tỉ lệ run ok là 30,00% ở lần 1, 11,43% ở lần 2, 2,15% ở lần 3. Lỗi lặp lại trên cùng yêu cầu, chạy lại chỉ tốn thêm tiền.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 982 yêu cầu, 900 việc thành công. Chi phí biến đổi mỗi việc thành công = 3.072.513 / 900 = 3.414 đ [simulated].

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Ở 45.000 yêu cầu/tháng, chi phí cố định không đổi kết luận (0,38× [simulated]). Khi còn một nửa khối lượng, chi phí cố định mỗi việc tăng gấp đôi lên 2.370 đ (0,48× [simulated]).
- Tính tay: cố định chỉ đẩy lên 12.000 đ khi còn dưới khoảng **6.200 yêu cầu/tháng** (40.000.000 / (12.000 − 3.414) × 1.200 / 900) [simulated]. Mức này chưa cộng phần chuyển nhân viên.

So sánh vận hành cùng mẫu số yêu cầu trong phạm vi, gồm nhân viên xử lý 82 ca không thành công và cố định: `(3.072.513,274 + 82 × 12.000) / 982 + 40.000.000 / (45.000 × 982 / 1.200)` = **5.217,09 đ/yêu cầu** [simulated]; ở nửa khối lượng là **6.303,31 đ/yêu cầu** [simulated]. Không dùng tỉ số CPS 0,38× thay cho so sánh đầy đủ này.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Chưa có chi phí cố định.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,07% |

Tự kiểm: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" (5,62 → 2,81; 40,70 → 20,35; 51,77 → 25,88). Đạt.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,31%)** [simulated], bằng tổng hai tác động riêng (5,62% + 40,70%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,77%) · 2. Tỉ lệ xem lại (+40,70%) · 3. Lương nhân viên (+23,12%) [simulated]. Giá token chỉ đứng sau cả ba (+5,62%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn **2 lần rẻ nhất cho công ty** (6.901.220 đ [simulated]). Mức này không trùng với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ [simulated]).
- Nếu chỉ tối ưu chi phí mỗi việc thành công (chọn 1 lần) thì đẩy thêm 85 ca sang nhân viên (319 − 234), làm cả hệ thống tốn thêm 548.560 đ [simulated].

## B4 · Nếu phải xem lại tất cả

- Xem lại 948 yêu cầu có run ok (5 phút/lần), 48 ca làm lại: **11.742,79 đ/việc** với 9 phút/ca; **12.414,50 đ/việc = 1,03×** với trung bình chính xác 15,2973 phút/ca từ CSV [simulated]; chưa cộng cố định và phần chuyển nhân viên.
- Pilot phải học được hai điều: tỉ lệ xem lại có thể giảm an toàn xuống bao nhiêu, và mỗi lần xem lại có dưới mức hoà vốn **5,1 phút** (hoặc 4,8 phút nếu làm lại mất 15,3 phút) không [simulated].
