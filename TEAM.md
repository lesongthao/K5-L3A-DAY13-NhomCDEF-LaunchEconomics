# Team

## Thông tin nhóm

- Tên nhóm: NhomCDEF
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-NhomCDEF-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics · nhánh `main` · các PR đã gộp: #1, #2, #6, #7, #8, #9, #10, #11, #12, #13 và PR chốt cuối sau duyệt chéo Gate 2a.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Sông Thao | 2A202603534 | sirothao123@gmail.com | https://github.com/lesongthao | Người viết code (CP1–CP2), phụ trách `chi_so.md` (CP5), nhóm trưởng điều phối PR |
|   2 | Bùi Nguyên Dũng | 2A202603587 | dung208042@gmail.com | https://github.com/Nesto08 | Kiểm chứng A/B (`bang_chi_phi.md`), đổi người viết code D1/E1 (`src/lab13.py`) |
|   3 | Hoàng Văn Bảo | 2A202603549 | 26ai.baohv@vinuni.edu.vn | https://github.com/BaoAIuet | Người gắn nhãn 1 (CP3), phụ trách `pilot_plan.yaml` (CP4), phiếu chấm hội đồng (CP5) |
|   4 | Nguyễn Bá Quảng | 2A202603555 | nbquang04@gmail.com | https://github.com/nbquang04 | Người gắn nhãn 2 (CP3), giữ hồ sơ launch v0 (E3), báo cáo nhóm |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao (từ Lê Sông Thao ở CP1–CP2 sang Bùi Nguyên Dũng ở CP4), để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## LeSongThao-2A202603534

### Phần việc phụ trách

- Khởi tạo repo nhóm (`K5-L3A-DAY13-NhomCDEF-LaunchEconomics`), mời 3 thành viên và điều phối quy trình làm việc theo nhánh riêng và Pull Request (PR).
- Người viết code chặng 1 (CP1–CP2): cài đặt Nhiệm vụ A (A1–A4) và B (B1–B4) trong `src/lab13.py`.
- Phụ trách Nhiệm vụ E1–E2 (CP5): hoàn thiện `report/team/chi_so.md` (5 chỉ số, 10 event có `trace_id`, đối chiếu chéo và bảng 3 rủi ro kinh tế).
- Rà soát, kiểm thử và gộp PR của các thành viên vào `main`; chủ trì duyệt chéo với NhomTTBH và đóng gói chốt nộp bài.

### Đóng góp cụ thể

- Hoàn thiện 3 phép thử A1 đạt 100% (`1,20 · 1,25 · 1,25`) và mô hình chi phí A2 (`CPS = 4.472 đ` `simulated`, gấp `16,3×` hoá đơn `274,7 đ/yêu cầu`; chi phí cả hệ thống/yêu cầu `5.865 đ = 0,49×` `simulated`).
- Tách chi phí theo loại A3 (`noi_dia` `2.696 đ = 0,22×`, `hang_nang` `8.221 đ = 0,69×`, `quoc_te` `22.515 đ = 1,88×` có tỉ lệ `ok` giảm `30,0% → 11,4% → 2,2%`, `doi_tac` `10.215 đ = 0,85×`, `simulated`) và phân bổ chi phí cố định 40 triệu đ/tháng A4 (`4.599 đ = 0,38×` ở 45.000 yc/tháng và `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- Cài đặt bảng độ nhạy B1–B4: xác định top 3 yếu tố nhạy nhất (`1. Số ca làm lại +51,8% · 2. Tỉ lệ xem lại +40,7% · 3. Lương nhân viên +23,1%`, `simulated`), đổi cặp `6.543 đ (+46,3%)` (`simulated`), giới hạn 2 lần chạy rẻ nhất cả hệ thống (`6.901.220 đ` `simulated`), và kịch bản xem lại 100% B4 ở 2 mốc làm lại (`11.743 đ = 0,98×` với 9,0 phút/ca và `12.415 đ = 1,03×` với 15,3 phút/ca, `simulated`).
- Hoàn thiện `report/team/chi_so.md`: 3 chỉ số tính thử E1 (`82,83%`, `27,12%`, `4,25%`; phạm vi `noi_dia + hang_nang` là `3,97%`), 2 chỉ số tự đề xuất, 10 event có `trace_id` kèm kiểm tra chéo và 3 dòng rủi ro kinh tế (`simulated`).
- Chuẩn hóa toàn bộ hồ sơ trước duyệt chéo Gate 2a và tổng hợp kết quả duyệt chéo với NhomTTBH (`30/30`).

### Bằng chứng

- PR #1 (`feat/thao-cost-model`, commit `ae97be1`, merge `03258a1`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/1 — `src/lab13.py`.
- PR #2 (`feat/thao-metrics-risk`, commit `518545f`, merge `b26318b`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/2 — `report/team/chi_so.md`.
- PR #6 (`docs/thao-personal-report`, commit `15d5339`, merge `29cdc57`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/6 — `report/team/2A202603534_LeSongThao.md`.
- PR #10 (`21be7df`), PR #13 (`0f55a11`) và nhánh `docs/final-gate2a-submission`: chuẩn hóa `TEAM.md`, `bang_loi.md`, `phieu_cham.md` và `group_report.md`.

## BuiNguyenDung-2A202603587

### Phần việc phụ trách

- CP1–CP2: Kiểm chứng kết quả A1–A4, B1–B4 và hoàn thiện `report/team/bang_chi_phi.md`.
- CP4–CP5: Bổ sung code D1 (cỡ mẫu, ICC, power) và E1 (ba chỉ số) vào `src/lab13.py`.

### Đóng góp cụ thể

- Chạy và đối chiếu mô hình chi phí với hai CSV giả lập; xác nhận ba phép thử A1 đạt.
- Hoàn thiện báo cáo A/B với CPS **4.472 đ (simulated)**; xác định giới hạn 2 lần chạy có tổng chi phí hệ thống thấp nhất **6.901.220 đ (simulated)**.
- Triển khai D1: tính cỡ mẫu **1.251 yêu cầu/nhóm**, điều chỉnh theo cụm **3.103 yêu cầu/nhóm**, power **0,642**.
- Triển khai E1: tính ba chỉ số **82,83%**, **27,12%**, **4,25%** trên CSV giả lập.
- Chạy lại `python lab13.py`, xác nhận A/B và D1/E1 hoạt động không có lỗi thực thi.

### Bằng chứng

- [PR #7](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/7) (commit `f927f03`, merge `f5762c0`): `report/team/bang_chi_phi.md` và phần D1/E1 trong `src/lab13.py`.
- [Báo cáo cá nhân](report/team/2A202603587_BuiNguyenDung.md) (commit `ea09874`, `86789d6`).
- Kết quả terminal `python lab13.py` (A1 đạt, A/B/D1/E1 chạy thành công).

## HoangVanBao-2A202603549

### Phần việc phụ trách

- Soát điều kiện hoàn thành CP1–CP2 theo đề và `RUBRIC.md`.
- Người gắn nhãn 1 (CP3): gắn nhãn 20 ca lỗi theo năm loại của Google PAIR, đối chiếu với Quảng và hoàn thiện bảng khắc phục 5 loại (`report/team/bang_loi.md`).
- Phụ trách Nhiệm vụ D (CP4): xây dựng kế hoạch pilot có đối chứng trong `report/team/pilot_plan.yaml`.
- Phụ trách chuẩn bị và ghi nhận phiếu duyệt chéo Gate 2a (`report/team/phieu_cham.md`).

### Đóng góp cụ thể

- Đối chiếu 20 ca lỗi với bộ nhãn của Quảng đạt đồng thuận **16/20 = 80%**, thống nhất quy tắc phân biệt cho 4 ca lệch (4, 14, 15, 18) và hoàn thiện bảng khắc phục 5 ca đủ năm loại.
- Thiết kế `report/team/pilot_plan.yaml`: phân ngẫu nhiên theo nhân viên 20 + 20, MDE +6 điểm %, `m ≥ 299`, `DE = 6,96`, công khai power **0,642** ở mức +5 điểm %, 4 luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, rollback 30 phút, tỷ lệ mở lại phạm vi pilot `39/982 = 3,97%` (`simulated`); đọc hợp lệ bằng `yaml.safe_load`.
- Hoàn thiện phiếu chấm `report/team/phieu_cham.md` đánh giá NhomTTBH đạt `30/30` (`Go có điều kiện`) cùng câu hỏi và phần xác nhận của đội bạn tại phiên duyệt chéo Gate 2a.

### Bằng chứng

- [PR #9](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/9) (commit `2392b18`, merge `e927958`): `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/phieu_cham.md`, `report/team/2A202603549_HoangVanBao.md`.
- Bản chốt `report/team/phieu_cham.md` sau phiên duyệt chéo với NhomTTBH.

## NguyenBaQuang-2A202603555

### Phần việc phụ trách

- Người gắn nhãn 2 (CP3): gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR và đối chiếu bảng lỗi với Bảo (`report/team/bang_loi.md`).
- Giữ hồ sơ Launch v0 (E3): tổng hợp đầy đủ 7 mục, gắn nhãn `simulated` và đề xuất `Go có điều kiện` trong `report/team/ho_so_launch_v0.md`.
- Tổng hợp báo cáo nhóm (`report/team/group_report.md`) và hoàn thiện báo cáo cá nhân (`report/team/2A202603555_NguyenBaQuang.md`).

### Đóng góp cụ thể

- Hoàn thiện bộ 20 nhãn người 2, đạt tỷ lệ trùng với cột người 1 là **16/20 = 80%** và đối chiếu quy tắc phân biệt cho 4 ca lệch.
- Tổng hợp đầy đủ 7 mục hồ sơ trong `report/team/ho_so_launch_v0.md`, ghi trạng thái `Giả lập` cho mục 1, 2, 3, 7, giữ nhãn `simulated` cho chi phí dẫn xuất, nêu cả các con số bất lợi và chốt phạm vi pilot `noi_dia + hang_nang` kèm điều kiện, vai trò, ngày kiểm tra.
- Chạy kiểm chứng `python lab13.py` (A1–B4, D1, E1), đọc kiểm tra YAML và bốn luật dừng; hoàn thiện `report/team/group_report.md` và báo cáo cá nhân.

### Bằng chứng

- [PR #8](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/8) (commit `7cdbeb5`, merge `c33de17`): hồ sơ ban đầu và bộ nhãn người 2.
- [PR #11](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/11) (commit `3064ada`, merge `ba6e00b`): chốt hồ sơ `Go có điều kiện` và hai báo cáo.
- [PR #12](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/12) (commit `f469b00`, merge `3d508b0`): chuẩn hóa hồ sơ, báo cáo cá nhân và thông tin thành viên.
- [Báo cáo cá nhân](report/team/2A202603555_NguyenBaQuang.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [báo cáo nhóm](report/team/group_report.md).
