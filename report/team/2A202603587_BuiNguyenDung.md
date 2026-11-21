# Báo cáo cá nhân — Bùi Nguyên Dũng — 2A202603587

## 1. Thông tin thành viên

- Họ tên: Bùi Nguyên Dũng
- MSSV: 2A202603587
- GitHub: https://github.com/Nesto08
- Email: dung208042@gmail.com
- Vai trò: Kiểm số A/B, hoàn thiện báo cáo chi phí; bổ sung code D1 (cỡ mẫu, power), E1 (3 chỉ số).

## 2. Phần việc phụ trách

- Kiểm tra kết quả Nhiệm vụ A1–A4, B1–B4 từ code nhóm và hai CSV giả lập của lab.
- Hoàn thiện `report/team/bang_chi_phi.md` (CP1–CP2).
- Sau khi PR #1 được merge, bổ sung code D1 (cỡ mẫu, ICC, power) và E1 (ba chỉ số) vào `src/lab13.py` (CP4–CP5).

## 3. Đóng góp cụ thể

- Chạy và kiểm tra `python lab13.py` trên code A/B đã merge; cả ba phép thử A1 đều **ĐẠT**.
- Đối chiếu kết quả A2–B4 và hoàn thiện bảng chi phí: tổng **4.373.585 đ**, **978** việc thành công, CPS **4.472 đ (simulated)**; giới hạn **2 lần chạy** cho chi phí toàn hệ thống thấp nhất **6.901.220 đ (simulated)**.
- Bổ sung D1 vào `src/lab13.py`: tính cỡ mẫu **1.251 yêu cầu/nhóm**, điều chỉnh theo cụm **3.103 yêu cầu/nhóm**, **42 nhân viên/nhóm**, power **0,642** ở kịch bản kiểm tra.
- Bổ sung E1 với ba chỉ số trên CSV giả lập: chỉ số chính **82,83%**, bỏ qua gợi ý **27,12%**, mở lại trong 7 ngày **4,25%**.
- Chạy lại `python lab13.py` và xác nhận A/B vẫn hoạt động, D1/E1 xuất kết quả đầy đủ, không có traceback.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md` — báo cáo A1–A4, B1–B4.
- `src/lab13.py` — code D1/E1, giữ nguyên phần A/B của nhóm.
- Kết quả terminal `python lab13.py` — ba phép thử A1 đạt, chương trình chạy hết A/B/D1/E1.
- Pull Request: f927f03b98dd70813356fd12ba0d0a209378e7c5

## 5. Công cụ AI đã dùng

- **ChatGPT:** hỗ trợ đọc yêu cầu lab, giải thích công thức, kiểm tra tính nhất quán của kết quả, dự thảo báo cáo A/B và hỗ trợ bổ sung code D1/E1.
- **Tự kiểm chứng:** chạy chương trình trên máy, đối chiếu kết quả với hai CSV giả lập và tài liệu `docs/du_lieu_va_cong_thuc.md`; không sử dụng câu trả lời AI thay thế bằng chứng thực nghiệm.

## 6. Tự đánh giá

- Đã hoàn thiện nội dung báo cáo A/B và triển khai code D1/E1; chương trình chạy thành công trên máy với dữ liệu giả lập của lab.
- Kết quả D1 cho thấy thiết kế chỉ có 20 nhân viên/nhóm chưa đủ cỡ mẫu hiệu dụng để phát hiện mức cải thiện 5 điểm phần trăm theo các giả định của bài.
