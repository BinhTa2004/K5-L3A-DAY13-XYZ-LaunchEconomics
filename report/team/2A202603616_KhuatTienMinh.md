# Báo cáo cá nhân — Khuất Tiến Minh — 2A202603616

Trạng thái: đã hoàn thành toàn bộ phần việc của Minh gồm Nhiệm vụ C (`report/team/bang_loi.md` với đồng thuận 20/20 = 100% cùng bộ nhãn độc lập của Dũng ở `0a72f5f`) và Nhiệm vụ D (`src/lab13.py` tích hợp `tinh_co_mau_d1` / `in_phan_d` chạy trọn bộ A–B–D1–E1 và `report/team/pilot_plan.yaml`). Phân công và bàn giao: [TEAM.md](../../TEAM.md).

## 1. Thông tin thành viên

- Họ tên: Khuất Tiến Minh
- MSSV: 2A202603616
- GitHub: Minhktm02
- Vai trong nhóm: Người gắn nhãn 1; bảng lỗi C; người viết code D1 sau giải lao và kế hoạch pilot D.

## 2. Phần việc được giao

- Gắn độc lập 20 ca trước khi xem nhãn Dũng hoặc đáp án tham khảo; giữ nguyên bộ nhãn gốc.
- Sau khi cả hai khóa nhãn, tổng hợp `bang_loi.md`: hai bộ nhãn, đồng thuận, quy tắc và năm cách khắc phục.
- Nhận code A–B đã tích hợp từ Bình, viết D1 vào `src/lab13.py`; hoàn thiện `pilot_plan.yaml`, giải thích đánh đổi và kiểm YAML; bàn giao code lại cho Bình.

## 3. Đóng góp cụ thể đã thực hiện

- **Nhánh làm việc:** tạo nhánh `day13/minh-errors-pilot` từ `main` đúng quy ước trong `TEAM.md`.
- **Nhiệm vụ C (`report/team/bang_loi.md`):**
  - Tự làm: đọc 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và 5 định nghĩa Google PAIR (không xem nhãn tham khảo), gắn độc lập 20 nhãn cho cột Người gắn nhãn 1 (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm) và khóa bản gốc.
  - Phối hợp: merge bộ nhãn độc lập của Nguyễn Tuấn Dũng (`report/team/nhan_dung_doc_lap.md`, commit `0a72f5f`), chép nguyên bộ nhãn vào cột Người gắn nhãn 2, tính đồng thuận đạt **20/20 = 100%** (không sửa lại nhãn gốc), bổ sung quy tắc phân biệt cho các ca ranh giới dễ nhầm (Ca 13, 9, 7–8).
  - Tự làm: hoàn thiện bảng khắc phục 5 ca đại diện đủ 5 loại (Ca 1, 20, 18, 13, 5) với event/ngưỡng/tần suất đo được và vai trò phụ trách cụ thể.
- **Nhiệm vụ D (`src/lab13.py` và `report/team/pilot_plan.yaml`):**
  - Tự làm: sau khi merge `origin/main` (commit `4bdce40` của Bình), bổ sung hàm `tinh_co_mau_d1(reqs)` và `in_phan_d(reqs)` vào `src/lab13.py` dùng `statsmodels` (`proportion_effectsize`, `NormalIndPower`) tính 5 câu D1 và tỉ lệ `mo_lai_trong_7_ngay`, chạy trọn bộ `python lab13.py` cùng test của Bình (`test_lab13.py`) đều ĐẠT.
  - Tự làm: hoàn thiện `report/team/pilot_plan.yaml` gồm chú thích D1–D2, giải thích đánh đổi chọn `unit: staff` (20 nhân viên/nhóm, nới MDE lên +6 điểm, m ≥ 299, DEFF = 6,96, `n_per_arm = 5980`), 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, rollback và liệt kê đầy đủ đầu vào `simulated`.
  - Phối hợp: sẵn sàng để Long kiểm độc lập số D1 và Dũng đối chiếu với `ho_so_launch_v0.md`.

## 4. Bằng chứng

- **File đã sửa trên nhánh `day13/minh-errors-pilot` (đã merge `origin/main` tới `4bdce40`):**
  - `report/team/bang_loi.md`
  - `src/lab13.py` (bổ sung `tinh_co_mau_d1` và `in_phan_d` tại mục CP4, giữ nguyên toàn bộ A–B và E1 của Bình)
  - `report/team/pilot_plan.yaml`
  - `report/team/2A202603616_KhuatTienMinh.md`
- **Lệnh đã chạy và kết quả kiểm tra (trong `src/` dùng `.venv`):**
  - Chạy trọn bộ `src/lab13.py`: `.\.venv\Scripts\python.exe lab13.py` -> in `Ba phép thử đáp án biết trước: ĐẠT`, đủ bảng A1–A4, B1–B4, D1 và E1.
  - Chạy bộ test `src/test_lab13.py`: `.\.venv\Scripts\python.exe -m unittest test_lab13.py -v` -> toàn bộ test ĐẠT.
  - Kết quả D1: a) `1.250` yêu cầu/nhóm (`raw=1.249,58`); b) `DEFF=2,48`, `3.100` yêu cầu/nhóm, `42` nhân viên/nhóm (tổng 84 > 40 -> không đủ); c) `n_eff < 1.000`/nhóm (< 1.250); d) `n_eff < 300`/nhóm; e) `m >= 299` yêu cầu/nhân viên (`DEFF=6,96`, `5.980` yêu cầu/nhóm, `n_eff=859,2`).
  - Tỉ lệ `mo_lai_trong_7_ngay` từ `logix_requests.csv`: toàn mẫu `4,25%` (51/1.200); phạm vi `noi_dia + hang_nang` là `3,97%` (`noi_dia` `3,16%`, `hang_nang` `8,23%`).
  - Kiểm tra YAML đọc được: `.\.venv\Scripts\python.exe -c "import yaml; d = yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8')); print(list(d['pilot'].keys()))"` -> ĐẠT.
  - Kiểm tra không còn dấu `?` ngoài chú thích và tuân thủ quy tắc thuật ngữ Gate 2a (chỉ dùng phạm vi pilot) trong `bang_loi.md`, `pilot_plan.yaml` -> ĐẠT.
  - Lưu ý nhãn `simulated`: các số chi phí xem lại/làm lại dùng để đối chiếu phạm vi `noi_dia + hang_nang` lấy từ hai cột `phut_xem_lai_simulated` và `phut_lam_lai_simulated` đã được ghi rõ nhãn `simulated` trong `pilot_plan.yaml`.

## 5. Công cụ AI đã dùng

- Khung phân công và mẫu báo cáo ban đầu được chuẩn bị với ChatGPT/Codex (theo ghi chú ở `TEAM.md`).
- Trong phần bài làm của Minh: dùng trợ lý AI (Antigravity / Gemini) để đọc đề bài `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, cài môi trường `.venv`, viết hàm tính cỡ mẫu D1 bằng `statsmodels`, kiểm tra cú pháp YAML và soát checklist nộp bài.
- Cách tự kiểm tra: đối chiếu kết quả `statsmodels` với công thức giải tích trong `docs/du_lieu_va_cong_thuc.md` (`1.250` vs `1.251`, lệch < 0,1%), chạy `yaml.safe_load`, kiểm tra regex không còn dấu `?` ngoài chú thích và không dùng từ cấm vượt phạm vi pilot, giữ nguyên bộ nhãn độc lập không xem đáp án tham khảo.

## 6. Tự đánh giá

- **Đã đạt:** hoàn thành và kiểm chứng đầy đủ toàn bộ phần C (`bang_loi.md` đạt đồng thuận 20/20 = 100% giữa hai bộ nhãn độc lập, đủ 5 loại lỗi và cách khắc phục đo được) và phần D (`src/lab13.py` chạy thông suốt A–B–D1–E1 cùng 12/12 test `test_lab13.py`, `pilot_plan.yaml` đọc được và đạt checklist).
- **Hạn chế:** chưa cần chỉnh sửa thêm ở phần Minh; sẵn sàng để Long kiểm độc lập số D1, Dũng cập nhật mục 5–6 vào `ho_so_launch_v0.md` và Bình tích hợp PR vào `main`.
- **Cải thiện:** khi bảo vệ trước hội đồng Gate 2a cần chuẩn bị giải thích rõ hai điểm trọng tâm: (1) lý do gắn nhãn theo nguyên nhân gốc cho Ca 13/9/7–8 và (2) đánh đổi nới MDE từ +5 lên +6 điểm khi chọn `unit: staff` (20 cụm/nhóm) để tránh spillover.
