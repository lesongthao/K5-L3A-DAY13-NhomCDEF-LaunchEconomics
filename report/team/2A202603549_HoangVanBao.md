# Báo cáo cá nhân — Hoàng Văn Bảo

## 1. Thông tin thành viên

- Họ tên: Hoàng Văn Bảo
- MSSV: 2A202603549
- Email: 26ai.baohv@vinuni.edu.vn
- Nhóm: CDEF · Lớp: L3A
- GitHub: @BaoAIuet
- Vai trò: Người gắn nhãn 1, phụ trách kế hoạch pilot và phiếu duyệt chéo.

## 2. Phần việc phụ trách

- Soát điều kiện hoàn thành CP1–CP2 theo đề và rubric.
- Gắn nhãn 20 ca lỗi CP3, đối chiếu với Quảng khi có bộ nhãn gốc, và chuẩn bị phương án khắc phục.
- Lập kế hoạch pilot CP4 và tham gia chấm nhóm được phân công ở CP5.

## 3. Đóng góp cụ thể

- **CP1–CP2:** Soát điều kiện hoàn thành và kiểm tra đầu ra của `src/lab13.py`. Cả ba phép thử A1 đạt (1,20 · 1,25 · 1,25) và chương trình in đủ 9 kịch bản B1.
- **CP3:** Tổng hợp bộ 20 nhãn Bảo cập nhật và 20 nhãn gốc của Quảng. Bộ nhãn Bảo gửi lại sau đối chiếu trùng 16/20 ca (80%). Bảo chọn nhãn Quảng đã nộp cho các ca 4, 14, 15 và 18 để hoàn tất cột nhãn thống nhất. Bảng khắc phục có đủ năm loại lỗi.
- **CP4:** Soạn kế hoạch pilot so sánh hai nhóm đồng thời, phân ngẫu nhiên theo nhân viên và cân bằng theo depot. Phương án cần 20 nhân viên mỗi nhóm và ít nhất 299 yêu cầu đủ điều kiện mỗi người. Nếu hiệu ứng thật là +5 điểm phần trăm, power chỉ đạt 0,642. Tỷ lệ mở lại trong phạm vi pilot là 39/982 = 3,97% [simulated]. Kế hoạch có bốn luật dừng và đã kiểm tra bằng `yaml.safe_load`.
- **CP5:** Chuẩn bị phiếu chấm theo ba tiêu chí của rubric và câu hỏi về cách xử lý khi chưa đạt cỡ mẫu vào ngày dự kiến. Điểm và quyết định hội đồng chờ hồ sơ nhóm được chấm và buổi duyệt chéo.

## 4. Bằng chứng

- [Bảng lỗi](bang_loi.md)
- [Kế hoạch pilot](pilot_plan.yaml)
- [Phiếu duyệt chéo](phieu_cham.md)
- [PR #9 — Phần Lab 13 của Bảo](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/9)

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc rubric, rà soát cấu trúc YAML, kiểm tra định dạng bảng và gợi ý nhãn tham khảo. Việc kiểm tra gồm tính lại tỷ lệ trùng từ hai cột nhãn, đối chiếu năm kết quả D1 với đầu ra của `src/lab13.py` và đọc tệp pilot bằng `yaml.safe_load`.

## 6. Tự đánh giá

Kế hoạch chọn chia theo nhân viên để giảm nguy cơ gợi ý lan sang nhóm đối chứng. Với 20 nhân viên mỗi nhóm, cỡ mẫu hiệu dụng luôn dưới 1.000, trong khi mục tiêu phát hiện chênh lệch 5 điểm phần trăm cần 1.251 mỗi nhóm. Kế hoạch vì vậy dùng mức chênh lệch 6 điểm phần trăm để thiết kế cỡ mẫu và yêu cầu xác nhận đủ 40 nhân viên trước khi chạy. Kết quả CP3 dựa trên bản nhãn cập nhật. CP5 còn chờ kết quả duyệt chéo.
