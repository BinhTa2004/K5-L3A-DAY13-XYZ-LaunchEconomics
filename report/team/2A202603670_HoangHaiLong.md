# Báo cáo cá nhân — Hoàng Hải Long — 2A202603670

Trạng thái: mới phân công, chưa ghi nhận kết quả thực hiện. Thông tin đối chiếu từ repo Day 08 của nhóm. Phân công và bàn giao: [TEAM.md](../../TEAM.md).

## 1. Thông tin thành viên

- Họ tên: Hoàng Hải Long
- MSSV: 2A202603670
- GitHub: hwangron
- Vai trong nhóm: Người kiểm số; bảng chi phí A–B, chỉ số và rủi ro E1–E2.

## 2. Phần việc được giao

- Tính tay ít nhất một khoản để đối chiếu output của Bình; điền A1–A4, B1–B4 trong `bang_chi_phi.md`.
- Kiểm độc lập cỡ mẫu D1 của Minh và phân biệt chi phí mỗi việc thành công với chi phí cả hệ thống.
- Hoàn thiện `chi_so.md`: ba chỉ số tính thử, hai chỉ số bổ sung, ít nhất sáu event có `trace_id`, ít nhất hai rủi ro có số; chuyển số chính cho Dũng.

## 3. Đóng góp cụ thể đã thực hiện

- Tự làm: kiểm số độc lập phần A (token, tool, xem lại, làm lại, chi phí mỗi việc thành công, dòng quoc_te ở A3) bằng script riêng, không gọi `lab13.py`.
- Tự làm: điền toàn bộ `bang_chi_phi.md` (A1–A4, B1–B4) và câu trả lời. Tính tay thêm mức khối lượng hoà vốn ở A4 (khoảng 6.200 yêu cầu/tháng [simulated]) và chênh lệch chi phí cả hệ thống ở B3 (548.560 đ [simulated]).
- Tự làm: viết `chi_so.md`: 3 chỉ số tính thử, 2 chỉ số tự đề xuất, 9 event có `trace_id`, kiểm tra chéo chỉ số với event, 3 dòng rủi ro kinh tế.
- Phối hợp: dùng output A–B và E1 của Bình (commit `4bdce40`). Phần kiểm độc lập D1 của Minh chưa làm vì D1 chưa có trong code.

## 4. Bằng chứng

- Nhánh `day13/long-cost-metrics`. File đã sửa: `report/team/bang_chi_phi.md`, `report/team/chi_so.md`.
- Lệnh đã chạy: `cd src && python lab13.py` in "Ba phép thử đáp án biết trước: ĐẠT" (1,20 · 1,25 · 1,25).
- Kiểm độc lập: token = 5.771.712 / 1.000 × 26 + 734.774 / 1.000 × 130 = 245.585,13 đ; tool = 5.600 × 15 = 84.000 đ; chi phí mỗi việc thành công = 4.373.585,13 / 978 = 4.471,97 đ [simulated]. Lệch 0% so với output của Bình.
- B1: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (5,62 → 2,81; 40,70 → 20,35; 51,77 → 25,88).
- `grep -rni production report/team` không in gì.

## 5. Công cụ AI đã dùng

- Claude Code (Claude Opus): đọc đề, lập kế hoạch, viết script kiểm số độc lập, soạn nội dung `bang_chi_phi.md` và `chi_so.md` từ output của `lab13.py`.
- Cách tự kiểm tra: mọi số đều lấy từ output `lab13.py` hoặc từ script kiểm độc lập (đọc trực tiếp CSV), rồi so với số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch không quá 2%). Không dùng AI để bịa số.

## 6. Tự đánh giá

Chưa cập nhật. Thành viên tự nêu kết quả, hạn chế và điều cần cải thiện sau khi làm.
