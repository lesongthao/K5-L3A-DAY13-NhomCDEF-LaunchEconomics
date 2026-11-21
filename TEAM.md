# Team

## Thông tin nhóm

- Tên nhóm: NhomCDEF
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-NhomCDEF-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics · nhánh `main` · commit chốt: cập nhật ở commit đóng gói cuối buổi sau khi đủ đóng góp của 4 thành viên.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Lê Sông Thao | 2A202603534 | sirothao123@gmail.com | https://github.com/lesongthao | Người viết code (CP1–CP2), phụ trách `chi_so.md` (CP5), nhóm trưởng điều phối PR |
|   2 |Bùi Nguyên Dũng|2A202603587|dung208042@gmail.com|https://github.com/Nesto08|	Kiểm chứng A/B, báo cáo chi phí, code D1/E1|
|   3 |        |      |       |        |         |
|   4 | Nguyễn Bá Quảng | 2A202603555 | nbquang04@gmail.com | https://github.com/nbquang04 | Người gắn nhãn 2 (C), giữ hồ sơ launch v0 (E3), báo cáo nhóm |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## LeSongThao-2A202603534

### Phần việc phụ trách

- Khởi tạo repo nhóm (`K5-L3A-DAY13-NhomCDEF-LaunchEconomics`), mời 3 thành viên và điều phối quy trình làm việc theo nhánh riêng và Pull Request (PR).
- Người viết code chặng 1 (CP1–CP2): cài đặt Nhiệm vụ A (A1–A4) và B (B1–B4) trong `src/lab13.py`.
- Phụ trách Nhiệm vụ E1–E2 (CP5): hoàn thiện `report/team/chi_so.md` (5 chỉ số, 10 event có `trace_id`, đối chiếu chéo và bảng 3 rủi ro kinh tế).
- Rà soát, kiểm thử và gộp PR của các thành viên vào `main`.

### Đóng góp cụ thể

- Hoàn thiện 3 phép thử A1 đạt 100% (`1,20 · 1,25 · 1,25`) và mô hình chi phí A2 (`CPS = 4.472 đ` `simulated`, gấp `16,3×` hoá đơn `274,7 đ/yêu cầu`; chi phí cả hệ thống/yêu cầu `5.865 đ = 0,49×` `simulated`).
- Tách chi phí theo loại A3 (`noi_dia` `2.696 đ = 0,22×`, `hang_nang` `8.221 đ = 0,69×`, `quoc_te` `22.515 đ = 1,88×` có tỉ lệ `ok` giảm `30,0% → 11,4% → 2,2%`, `doi_tac` `10.215 đ = 0,85×`, `simulated`) và phân bổ chi phí cố định 40 triệu đ/tháng A4 (`4.599 đ = 0,38×` ở 45.000 yc/tháng và `5.784 đ = 0,48×` ở nửa khối lượng, `simulated`).
- Cài đặt bảng độ nhạy B1–B4: xác định top 3 yếu tố nhạy nhất (`1. Số ca làm lại +51,8% · 2. Tỉ lệ xem lại +40,7% · 3. Lương nhân viên +23,1%`, `simulated`), đổi cặp `6.543 đ (+46,3%)` (`simulated`), giới hạn 2 lần chạy rẻ nhất cả hệ thống (`6.901.220 đ` `simulated`), và kịch bản xem lại 100% B4 ở 2 mốc làm lại (`11.743 đ = 0,98×` với 9,0 phút/ca và `12.415 đ = 1,03×` với 15,3 phút/ca, `simulated`).
- Hoàn thiện `report/team/chi_so.md`: 3 chỉ số tính thử E1 (`82,83%`, `27,12%`, `4,25%`; phạm vi `noi_dia + hang_nang` là `3,97%`), 2 chỉ số tự đề xuất, 10 event có `trace_id` kèm kiểm tra chéo và 3 dòng rủi ro kinh tế (`simulated`).

### Bằng chứng

- PR #1 (`feat/thao-cost-model`, commit `ae97be1`, merge `03258a1`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/1 — `src/lab13.py`.
- PR #2 (`feat/thao-metrics-risk`, commit `518545f`, merge `b26318b`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/2 — `report/team/chi_so.md`.
- PR #6 (`docs/thao-personal-report`, commit `15d5339`, merge `29cdc57`): https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/6 — `report/team/2A202603534_LeSongThao.md`.

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

- `report/team/bang_chi_phi.md`
- `src/lab13.py`
- Kết quả terminal `python lab13.py` (A1 đạt, A/B/D1/E1 chạy thành công).

## NguyenBaQuang-2A202603555

### Phần việc phụ trách

- C: Bộ nhãn người 2 cho 20 ca lỗi, đối chiếu bảng lỗi với Bảo.
- E3: Tổng hợp hồ sơ launch v0 và đề xuất Go có điều kiện.
- Viết báo cáo nhóm và báo cáo cá nhân.

### Đóng góp cụ thể

- Điền 7 mục hồ sơ, ghi trạng thái Giả lập cho mục 1, 2, 3, 7; giữ nhãn simulated cho chi phí dẫn xuất.
- Nêu cả số bất lợi và chốt phạm vi pilot nội địa + hàng nặng, có điều kiện, vai trò và ngày kiểm tra.
- Cung cấp 20 nhãn người 2; tỷ lệ trùng với cột người 1 là 16/20 = 80%; đối chiếu quy tắc cho bốn ca lệch.
- Chạy kiểm chứng A–B/D1/E1, đọc YAML và kiểm tra bốn luật dừng; hoàn thiện hai báo cáo.

### Bằng chứng

- [PR #8](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/8): hồ sơ ban đầu và bộ nhãn người 2.
- [PR #11](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/11): hồ sơ chốt và báo cáo.
- [Báo cáo cá nhân](report/team/2A202603555_NguyenBaQuang.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [báo cáo nhóm](report/team/group_report.md).
