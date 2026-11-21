# Team · Lab 13 · XYZ

## Thông tin nhóm

- Tên nhóm: XYZ (theo tên repo hiện tại).
- Lớp: L3A.
- Trưởng nhóm, tích hợp và nộp repo: Tạ Công Bình.
- Repo: https://github.com/BinhTa2004/K5-L3A-DAY13-XYZ-LaunchEconomics
- Nhánh tích hợp/nộp: `main`. Commit chốt bài sẽ bổ sung sau khi hoàn thành.
- Trạng thái: Bình đã triển khai code A–B và phép tính ba chỉ số E1, có 12 bài kiểm tra tự động đạt; chờ Long kiểm độc lập và Minh bổ sung D1. Hồ sơ của các thành viên tiếp tục hoàn thiện theo phân công.
- Họ tên, MSSV và GitHub đối chiếu từ `TEAM.md` cùng báo cáo cá nhân trong repo Day 08 `K5-L3A-DAY08-FPT-FromWorkflowsToAgents` của nhóm.

## Thành viên và phần việc

| STT | Họ tên | MSSV | GitHub | Vai trò và đầu việc |
| --: | --- | --- | --- | --- |
| 1 | Tạ Công Bình | 2A202603628 | BinhTa2004 | Viết code A–B; hỗ trợ tính E; tích hợp, kiểm tra và push bài chung |
| 2 | Hoàng Hải Long | 2A202603670 | hwangron | Kiểm số; bảng chi phí A–B; chỉ số, event và rủi ro E1–E2 |
| 3 | Khuất Tiến Minh | 2A202603616 | Minhktm02 | Gắn nhãn 1; tổng hợp C; viết code cỡ mẫu D1 sau giải lao và kế hoạch pilot D |
| 4 | Nguyễn Tuấn Dũng | 2A202603608 | dzungapr6th99 | Gắn nhãn 2, giữ hồ sơ; hồ sơ launch E3; báo cáo nhóm và phiếu duyệt chéo |

## Đầu việc và điều kiện bàn giao

| Người phụ trách | Phần phải làm | Bàn giao khi |
| --- | --- | --- |
| Bình | A1: ba hàm xác suất/chi phí; A2: `mo_hinh`; A3: bốn loại yêu cầu; A4: cố định ở hai mức khối lượng; B1–B4: độ nhạy, chạy lại và xem lại 100% | `src/lab13.py` in ba phép thử ĐẠT và đủ bảng A–B; chuyển output cho Long, chuyển code đã tích hợp cho Minh |
| Long | Tính tay ít nhất một khoản đối chiếu; điền A1–A4, B1–B4 vào bảng chi phí; kiểm chi phí cả hệ thống; E1: ba chỉ số có kết quả, thêm hai chỉ số, ít nhất sáu event có `trace_id`; E2: ít nhất hai rủi ro có số | `bang_chi_phi.md`, `chi_so.md` có công thức/nguồn số và nhãn `simulated` khi cần; gửi số chính cho Dũng; kiểm độc lập D1 của Minh |
| Minh | Gắn 20 ca độc lập; nhận bộ nhãn của Dũng sau khi cả hai khóa nhãn; tính đồng thuận, ghi quy tắc và năm cách khắc phục; viết D1 vào `lab13.py`, hoàn thiện D1–D3 trong YAML | `bang_loi.md` đủ hai bộ nhãn và năm loại lỗi; `pilot_plan.yaml` đủ trường, đọc được, không còn dấu hỏi ngoài chú thích, có ít nhất ba luật dừng bốn vế và giải thích đánh đổi cỡ mẫu |
| Dũng | Gắn 20 ca độc lập; kiểm bảng C sau tổng hợp; điền dần bảy mục hồ sơ launch; tổng hợp báo cáo nhóm; ghi phiếu chấm sau khi nhận hồ sơ nhóm khác | `ho_so_launch_v0.md` có số, trạng thái, vai trò phụ trách và đề xuất có căn cứ; `group_report.md` dẫn đúng bằng chứng; `phieu_cham.md` ghi đúng việc duyệt chéo thực tế |

Mọi thành viên tự điền báo cáo cá nhân, giải thích được phần mình và tự nộp link repo trên LMS.

## File do ai sửa

Các đường dẫn dưới đây tính từ root repo. Mỗi file có một người tổng hợp; người soát gửi nhận xét hoặc sửa qua nhánh riêng.

| File | Người ghi chính | Người kiểm |
| --- | --- | --- |
| `src/lab13.py` — A, B | Bình | Long |
| `src/lab13.py` — D1, sau khi A–B đã tích hợp | Minh | Long, Bình |
| `src/lab13.py` — phép tính ba chỉ số E, sau D1 | Bình | Long |
| `report/team/bang_chi_phi.md` | Long | Bình |
| `report/team/bang_loi.md` | Minh, sau khi cả hai khóa nhãn | Dũng |
| `report/team/pilot_plan.yaml` | Minh | Long kiểm mẫu/số; Dũng kiểm khớp hồ sơ |
| `report/team/chi_so.md` | Long | Bình kiểm công thức; Dũng kiểm nối với hồ sơ |
| `report/team/ho_so_launch_v0.md` | Dũng | Bình, Long, Minh soát phần mình |
| `report/team/group_report.md` | Dũng | Bình |
| `report/team/phieu_cham.md` | Dũng, ghi kết quả cả nhóm thảo luận | Minh |
| `TEAM.md` | Bình | Từng người xác nhận thông tin/đóng góp |
| Báo cáo cá nhân | Chính thành viên có tên trên file | Bình kiểm đủ file |

## Thứ tự và mốc bàn giao

Mốc giờ theo lịch mẫu trong [CHECKPOINTS.md](CHECKPOINTS.md), không phải lịch hẹn mới. Nếu coach đổi lịch, giữ thứ tự và thời lượng. Deadline nộp theo [SUBMISSION.md](SUBMISSION.md): trước 23:59 GMT+7 ngày lab.

| Mốc mẫu | Bình | Long | Minh | Dũng |
| --- | --- | --- | --- | --- |
| 14:00–14:10 | Chuẩn bị repo/môi trường | Kiểm dữ liệu/công thức | Đọc yêu cầu C, D | Mở hồ sơ và checklist |
| 14:10–14:53 · CP1 | Viết/chạy A1–A4 | Kiểm số, ghi bảng A | Chuẩn bị cấu trúc YAML, yêu cầu D1 | Lập khung bảy mục, ghi trạng thái Chưa |
| 14:53–15:20 · CP2 | Viết/chạy B1–B4, tích hợp A–B | Hoàn thiện bảng B | Chuẩn bị cách kiểm YAML/cỡ mẫu | Nhận số A–B vào hồ sơ |
| 15:35–16:08 · CP3 | Sửa/kiểm A–B nếu cần | Soát chi phí cả hệ thống | 8 phút gắn nhãn riêng; sau đó tổng hợp C | 8 phút gắn nhãn riêng; sau đó so/giải thích nhãn với Minh |
| 16:08–16:36 · CP4 | Bàn giao quyền sửa `lab13.py` cho Minh; soát tích hợp | Kiểm D1, chuẩn bị E1–E2 | Viết code D1, hoàn thiện YAML rồi bàn giao lại code | Soát phạm vi, luật dừng và cập nhật hồ sơ |
| 16:36–17:00 · CP5 | Tính ba chỉ số E trong code đã nhận lại | Hoàn thiện `chi_so.md` | Kiểm C, D và giả định | Chốt hồ sơ đủ bảy mục để duyệt chéo |
| 17:00–17:45 | Cùng bảo vệ/chấm theo bằng chứng | Giải thích chi phí/chỉ số | Giải thích lỗi/cỡ mẫu | Ghi phiếu chấm và phản hồi thực tế |
| 17:45–18:00 | Kiểm, tích hợp, push | Chốt số/báo cáo cá nhân | Chốt C, D/báo cáo cá nhân | Chốt hồ sơ/báo cáo nhóm/cá nhân |

## Làm độc lập phần nhãn C

1. Minh và Dũng chỉ đọc 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` cùng định nghĩa năm loại trước khi gắn nhãn. Chưa xem bộ nhãn của nhau hoặc mục nhãn tham khảo trong hướng dẫn chi tiết.
2. Mỗi người tự ghi đủ 20 nhãn trong 8 phút vào bản riêng, rồi khóa/lưu bản gốc trước khi trao đổi.
3. Sau đó Minh chép nguyên hai bộ nhãn vào `bang_loi.md`, tính đồng thuận; thống nhất ở cột riêng. Không sửa lại hai bộ nhãn độc lập sau khi so.
4. Nếu đồng thuận dưới 80%, ghi rõ định nghĩa đã chỉnh và quy tắc phân biệt; không điền tỷ lệ hoặc kết quả duyệt chéo khi chưa thực hiện.

## Lấy bài và gửi phần việc

Người chưa clone chạy:

```powershell
git clone https://github.com/BinhTa2004/K5-L3A-DAY13-XYZ-LaunchEconomics.git
cd K5-L3A-DAY13-XYZ-LaunchEconomics
```

Người đã clone, sau khi đã commit hoặc cất thay đổi đang làm, chạy:

```powershell
git switch main
git pull --ff-only origin main
```

Tạo nhánh riêng từ `main` mới nhất, chọn đúng dòng của mình:

| Người | Lệnh tạo nhánh |
| --- | --- |
| Bình | `git switch -c day13/binh-economics` |
| Long | `git switch -c day13/long-cost-metrics` |
| Minh | `git switch -c day13/minh-errors-pilot` |
| Dũng | `git switch -c day13/dung-launch-report` |

Chạy/cài Python theo [src/README.md](src/README.md). Mọi lệnh tính toán chạy trong `src/`.

- Chỉ commit file/phần mình được giao cùng báo cáo cá nhân. Push nhánh và mở pull request vào `main`; Bình kiểm và tích hợp. Nhánh trên là tên đề xuất, chưa được tạo sẵn.
- Khi Bình đã tích hợp A–B, Minh commit phần C/YAML đang làm, `git fetch origin` rồi `git merge origin/main` vào nhánh mình trước khi viết D1. Sau khi D1 tích hợp, Bình cũng cập nhật nhánh theo cách này trước khi thêm phép tính E. Không thay toàn bộ `lab13.py` bằng bản cũ.
- Nếu chưa có quyền push repo nhóm, push nhánh lên fork và mở pull request; Bình xử lý tích hợp. Không force-push.
- Khi bàn giao, ghi commit, lệnh đã chạy, kết quả kiểm và việc chưa xong. Bình cập nhật bảng bằng chứng bên dưới từ công việc thực tế.
- Không sửa CSV, `lab13_starter.py`, đề bài hoặc quy định. Giữ file mẫu báo cáo cá nhân. Mọi số dùng hai cột `_simulated` phải có nhãn `simulated`.

## Báo cáo cá nhân và bằng chứng thực tế

| Thành viên | Báo cáo cá nhân | Commit/kết quả thực tế |
| --- | --- | --- |
| Bình | [2A202603628_TaCongBinh.md](report/team/2A202603628_TaCongBinh.md) | Code A1–A4, B1–B4, ba chỉ số E1 trong `src/lab13.py`; `python -m unittest -v test_lab13`: 12/12 đạt; có ChatGPT/Codex hỗ trợ triển khai và kiểm tra; chờ Long soát độc lập |
| Long | [2A202603670_HoangHaiLong.md](report/team/2A202603670_HoangHaiLong.md) | Chưa ghi nhận; bổ sung sau khi làm |
| Minh | [2A202603616_KhuatTienMinh.md](report/team/2A202603616_KhuatTienMinh.md) | Chưa ghi nhận; bổ sung sau khi làm |
| Dũng | [2A202603608_NguyenTuanDung.md](report/team/2A202603608_NguyenTuanDung.md) | Chưa ghi nhận; bổ sung sau khi làm |

Bốn báo cáo đã tạo sẵn thông tin và phần việc dự kiến. Mỗi người tự bổ sung đóng góp, công cụ AI, cách kiểm tra và tự đánh giá sau khi thực hiện. Việc chuẩn bị phân công có ChatGPT/Codex hỗ trợ đọc repo Day 08 và yêu cầu Lab 13.

Phần tính E1 đã được Bình bổ sung sớm cùng A–B để Long có thể kiểm ngay. Minh giữ lời gọi `in_chi_so(reqs)` khi thêm D1 vào vị trí `TODO CP4` trong `main()`. Lệnh tái lập và ghi chú mô hình: [src/README.md](src/README.md).
