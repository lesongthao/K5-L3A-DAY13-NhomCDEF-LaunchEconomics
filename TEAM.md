# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |        |      |       |        |         |
|   2 |Bùi Nguyên Dũng|2A202603587|dung208042@gmail.com|https://github.com/Nesto08|	Kiểm chứng A/B, báo cáo chi phí, code D1/E1|
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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
