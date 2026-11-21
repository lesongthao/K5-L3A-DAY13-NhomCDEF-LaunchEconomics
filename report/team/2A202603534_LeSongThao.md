# Báo cáo cá nhân — LeSongThao-2A202603534

## 1. Thông tin thành viên

- Họ tên: Lê Sông Thao
- MSSV: `2A202603534`
- Email: `sirothao123@gmail.com`
- Nhóm / Lớp: `NhomCDEF` · Lớp `L3A`
- Vai trong nhóm: Người viết code (chặng 1: CP1–CP2), phụ trách đặc tả chỉ số và rủi ro kinh tế (CP5), nhóm trưởng điều phối quy trình Git/PR.

## 2. Phần việc phụ trách

- Khởi tạo repo `K5-L3A-DAY13-NhomCDEF-LaunchEconomics`, mời 3 thành viên và thiết lập quy trình nhánh riêng kết hợp Pull Request (PR) để tránh xung đột mã.
- Chặng 1 (CP1–CP2): cài đặt môi trường ảo `src/.venv` và triển khai toàn bộ Nhiệm vụ A (A1–A4) và Nhiệm vụ B (B1–B4) trong `src/lab13.py`.
- Nhiệm vụ E1–E2 (CP5): hoàn thiện `report/team/chi_so.md` gồm 5 chỉ số, 10 event có `trace_id`, bảng kiểm tra chéo và 3 dòng rủi ro kinh tế.
- Rà soát PR của thành viên, chốt `TEAM.md` và kiểm tra danh mục nộp bài vào cuối buổi.

## 3. Đóng góp cụ thể

- **Nhiệm vụ A1 (3 phép thử đáp án biết trước, `src/lab13.py`):** Cài đặt các hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; đạt 100% cả 3 phép thử (`1,20 · 1,25 · 1,25`).
- **Nhiệm vụ A2 (mô hình chi phí trên 1.200 yêu cầu / 1.624 lần chạy):** Token `245.585 đ` (`đo từ trace`), Tool `84.000 đ` (`đo từ trace`, phần lần chạy 2 và 3 là `93.804 đ`), Xem lại `1.780.000 đ` (`simulated`), Làm lại `2.264.000 đ` (`simulated`), Tổng `4.373.585 đ`, 978 việc thành công → **CPS = 4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token+tool chia số yêu cầu (`274,7 đ`). Giờ nhân viên chiếm `92,5%` tổng chi phí (`simulated`). Chi phí cả hệ thống mỗi yêu cầu (cộng 222 ca không thành công × 12.000 đ) là `5.865 đ = 0,49×` (`simulated`).
- **Nhiệm vụ A3 (tách theo loại yêu cầu, có phần `simulated`):** `noi_dia` `2.696 đ = 0,22×` (`simulated`), `hang_nang` `8.221 đ = 0,69×` (`simulated`), `quoc_te` `22.515 đ = 1,88×` (`simulated`, tỉ lệ `ok` giảm `30,0% → 11,4% → 2,2%` nên chạy lại không giúp), `doi_tac` `10.215 đ = 0,85×` (`simulated`). Đề xuất thu hẹp phạm vi pilot chỉ giữ `noi_dia` và `hang_nang`.
- **Nhiệm vụ A4 (chi phí cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang`):** Ở 45.000 yêu cầu/tháng (33.750 việc thành công), chi phí cố định là `1.185 đ/việc`, tổng CPS `4.599 đ = 0,38×` (`simulated`); ở một nửa khối lượng (16.875 việc), cố định tăng lên `2.370 đ/việc`, tổng CPS `5.784 đ = 0,48×` (`simulated`).
- **Nhiệm vụ B1–B2 (bảng độ nhạy 9 kịch bản & đổi cặp):** Tự kiểm chứng tính tuyến tính bằng `assert` (giảm nửa bằng đúng nửa mức tăng gấp đôi). Xếp hạng top 3 yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (`+51,8%` lên `6.787 đ` `simulated`) · 2. Tỉ lệ xem lại (`+40,7%` lên `6.292 đ` `simulated`) · 3. Lương nhân viên (`+23,1%` lên `5.506 đ` `simulated`)**. Đổi cặp Token ×2 + Xem lại ×2 ra `6.543 đ (+46,3%)` (`simulated`).
- **Nhiệm vụ B3 (giới hạn chạy lại và chi phí cả hệ thống):** 1 lần `7.449.781 đ` (`CPS 4.111 đ` `simulated`), **2 lần `6.901.220 đ` (rẻ nhất cho công ty, `CPS 4.237 đ` `simulated`)**, 3 lần `7.037.585 đ` (`CPS 4.472 đ` `simulated`).
- **Nhiệm vụ B4 (xem lại 100% trên `noi_dia` + `hang_nang`):** Với 948 ca xem lại 5 phút, 48 ca làm lại, 900 việc thành công và `224.513 đ` token+tool: ở mức 9,0 phút làm lại/ca (theo đề) cho tổng `10.568.513 đ` → CPS `11.743 đ = 0,98×` (`simulated`, hòa vốn xem lại `≤ 5,1 phút/ca`); ở mức trung bình dữ liệu `15,3 phút/ca` cho tổng `11.173.054 đ` → CPS `12.415 đ = 1,03×` (`simulated`, hòa vốn `≤ 4,8 phút/ca`).
- **Nhiệm vụ E1–E2 (`report/team/chi_so.md`):** Tính thử 3 chỉ số trên 1.200 yêu cầu: chỉ số chính `82,83%` (994/1.200, không kết luận trợ lý đã nâng chỉ số do chưa có nhóm đối chứng), tỉ lệ bỏ qua gợi ý `27,12%` (48/177), tỉ lệ mở lại 7 ngày `4,25%` (51/1.200; riêng phạm vi pilot `3,97%`, 39/982); đề xuất thêm 2 chỉ số dùng/an toàn, thiết kế 10 event có `trace_id` kèm đối chiếu chéo và lập bảng 3 rủi ro kinh tế (`simulated`).

## 4. Bằng chứng

- **PR #1** (nhánh `feat/thao-cost-model`, commit `ae97be1`, merge `03258a1`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/1 — hoàn thiện `src/lab13.py` (214 dòng, in `Ba phép thử đáp án biết trước: ĐẠT`, exit code `0`).
- **PR #2** (nhánh `feat/thao-metrics-risk`, commit `518545f`, merge `b26318b`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/2 — hoàn thiện `report/team/chi_so.md` (49 dòng, 10 event có `trace_id`, 3 dòng rủi ro kinh tế).
- **Nhánh `docs/thao-personal-report`**: báo cáo cá nhân `report/team/2A202603534_LeSongThao.md`.

## 5. Công cụ AI đã dùng

- **Công cụ sử dụng:** Antigravity.
- **Phạm vi hỗ trợ:** tham khảo nhanh các khái niệm kinh tế học tác tử (Cost-of-Pass, phân bổ chi phí cố định), rà soát cú pháp Type Hints trong Python, và kiểm tra đối chiếu định dạng bảng, quy tắc nộp bài trước khi tạo PR. Bản thân trực tiếp chủ trì phân công nhóm, quản lý nhánh Git, chạy kiểm thử thực tế trên dữ liệu và chịu trách nhiệm toàn bộ kết quả trong hồ sơ.
- **Cách tự kiểm tra kết quả:**
  1. Kích hoạt `src/.venv` chạy trực tiếp `python lab13.py` trên `logix_runs.csv` và `logix_requests.csv` (`keep_default_na=False`), xác nhận 3 phép thử A1 đạt `1,20 · 1,25 · 1,25` và kiểm chứng tuyến tính ở B1 đạt `assert`.
  2. Đối chiếu từng bảng A2–A4, B1–B4, E1 với công thức trong `docs/du_lieu_va_cong_thuc.md` và ngưỡng sai số ≤ 2%.
  3. Kiểm tra `git diff`, số dòng dưới 300, đầy đủ nhãn `simulated`, không chứa từ cấm và giữ nguyên trạng các file CSV cùng `src/lab13_starter.py`.

## 6. Tự đánh giá

- **Ưu điểm:** hoàn thành đúng tiến độ và giữ lịch sử Git sạch sẽ (PR #1, PR #2 đã merge không xung đột), cung cấp kịp thời số liệu gốc để nhóm triển khai các bước sau; nắm chắc bản chất chi phí thực của tác tử (giờ nhân viên chiếm 92,5% chi phí, khác biệt giữa CPS và chi phí cả hệ thống, vai trò event có `trace_id` để thay thế số giả lập sau tuần 1).
- **Điểm cần lưu ý:** tiếp tục theo sát khâu rà soát PR của các thành viên khác (đặc biệt quy trình gắn nhãn độc lập ở CP3 và tính nhất quán số liệu giữa `bang_chi_phi.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md`) và tổng hợp chốt đủ mã PR, commit cuối vào `TEAM.md` ở bước đóng gói 17:45.
