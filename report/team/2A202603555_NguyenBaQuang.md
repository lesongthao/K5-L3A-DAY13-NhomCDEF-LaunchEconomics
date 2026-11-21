# Báo cáo cá nhân — Nguyễn Bá Quảng — 2A202603555

## 1. Thông tin thành viên

- Họ tên: Nguyễn Bá Quảng
- MSSV: 2A202603555
- Email: nbquang04@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ launch; phụ trách báo cáo nhóm.

## 2. Phần việc phụ trách

Cung cấp bộ nhãn người 2 cho 20 ca lỗi; tổng hợp bằng chứng A–E vào hồ sơ launch v0; chuẩn bị báo cáo nhóm. Không phụ trách code mô hình, bộ nhãn người 1 hay pilot plan.

## 3. Đóng góp cụ thể

Hoàn thiện hồ sơ 7 mục từ kết quả A–E; ghi nhãn simulated, trạng thái Giả lập cho mục 1, 2, 3, 7 và một vai trò cụ thể phụ trách. Nêu số bất lợi: quốc tế 22.515 đ/việc và xem lại 100% có thể lên 12.415 đ/việc (simulated). Bổ sung chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49 lần mốc tự làm (simulated).

Điền 20 nhãn đề xuất vào cột người 2; chưa xác nhận hoàn thành lượt tự gắn nhãn trong 8 phút. Đối chiếu phần Bảo ở PR #9: bản cập nhật trùng 16/20 (80%), đủ 5 loại khắc phục, pilot có 4 luật dừng. Chốt đề xuất Go có điều kiện, nêu rõ vai trò và ngày kiểm tra theo lịch đề xuất; hoàn thiện báo cáo nhóm. Giữ ghi chú quy trình độc lập chưa được xác nhận và chưa có kết quả duyệt chéo.

## 4. Bằng chứng

- [PR #8](https://github.com/lesongthao/K5-L3A-DAY13-NhomCDEF-LaunchEconomics/pull/8), commit `7cdbeb5`: hồ sơ và bộ nhãn người 2.
- [Hồ sơ launch v0](ho_so_launch_v0.md), [bảng lỗi](bang_loi.md), [báo cáo nhóm](group_report.md).
- Đã chạy trọn bộ `python lab13.py`: A1 đạt, A–B/D1/E1 chạy thành công; đối chiếu E1 với CSV, đọc yêu cầu bằng `keep_default_na=False`. Kiểm tra `yaml.safe_load` đạt, đủ 4 luật dừng theo mẫu và không còn dấu hỏi; tính lại tỷ lệ trùng nhãn được 16/20.

## 5. Công cụ AI đã dùng

Dùng Codex đọc tài liệu, đề xuất bộ nhãn, tổng hợp hồ sơ, soạn báo cáo và thao tác Git/PR. Nhãn người 2 được AI đề xuất từ nội dung 20 ca, không xem nhãn người 1 hay bảng đáp án tham khảo. Đối chiếu chi phí với kết quả chạy code và các chỉ số với phép đếm trên CSV; cần tự rà soát và xác nhận bộ nhãn trước khi nộp.

## 6. Tự đánh giá

Đã hoàn thiện hồ sơ launch và báo cáo từ bằng chứng hiện có, nêu cả số bất lợi và điều kiện pilot. Hạn chế còn lại là quy trình nhãn độc lập chưa xác nhận, lịch pilot cần duyệt và kết quả duyệt chéo chưa có. Không tự xác nhận đã hoàn thành các điều kiện vận hành hoặc kết quả hội đồng.
