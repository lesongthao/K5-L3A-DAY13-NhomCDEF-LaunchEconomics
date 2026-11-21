# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: NhomCDEF
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Đánh giá tính kinh tế và điều kiện pilot trợ lý hoàn phí LogiX-VN tại Gate 2a. Nhóm tính chi phí từ trace, kiểm tra độ nhạy, phân loại nguyên nhân lỗi và thiết kế pilot có đối chứng. Dữ liệu lab là giả lập; kết quả chưa chứng minh hiệu quả nhân quả.

## 3. Giải pháp

A–B: mô hình và kiểm số trong [bảng chi phí](bang_chi_phi.md), code tại [lab13.py](../../src/lab13.py). C: [bảng lỗi](bang_loi.md) có đủ 20 ca, tỷ lệ trùng hai cột nhãn 16/20 (80%), bốn ca lệch đã thống nhất và đủ 5 loại khắc phục. D: [pilot plan](pilot_plan.yaml) đã có đối chứng đồng thời, 4 luật dừng và rollback 30 phút. E: [chỉ số và rủi ro](chi_so.md) quy định 10 event có `trace_id`; [hồ sơ launch](ho_so_launch_v0.md) tổng hợp bằng chứng.

## 4. Kết quả

CPS 4.472 đ/việc; chi phí cả hệ thống 5.865 đ/yêu cầu, bằng 0,49 lần mốc tự làm 12.000 đ (simulated). Quốc tế có CPS 22.515 đ; nội địa + hàng nặng khi xem lại 100% có CPS 11.743–12.415 đ (simulated), nên lợi ích phụ thuộc thời gian nhân viên. Ba yếu tố nhạy nhất: làm lại, xem lại và lương.

Chỉ số trong đợt chạy thử: đóng trong 24 giờ và không mở lại 7 ngày 82,83%; bỏ qua gợi ý 27,12%; mở lại 4,25%. Không có đối chứng để kết luận cải thiện. D1 yêu cầu 1.251 yêu cầu/nhóm, hoặc 3.103 yêu cầu và 42 nhân viên/nhóm khi DE = 2,48.

Đề xuất: **Go có điều kiện** cho pilot nội địa + hàng nặng tại D01–D06. Thiết kế chọn 20 nhân viên/nhóm, ≥299 yêu cầu/người, 5.980 yêu cầu thực/nhóm, DE 6,96, khoảng 859 hiệu dụng, MDE 6 điểm %. Power chỉ 0,642 nếu hiệu ứng thật 5 điểm %. Ngày 04/12/2026: Kỹ sư trưởng agent kiểm thử khắc phục 5 loại lỗi, Giám đốc vận hành xác nhận đủ 40 người và duyệt lịch. Ngày 07/12: Kế toán trưởng kiểm tra đo chi phí thật trước khởi động. Ngày 19/01/2027: Giám đốc vận hành xét quyết định theo cỡ mẫu, hiệu quả, an toàn và chi phí; thiếu mẫu thì chốt lại lịch trước khi đọc chỉ số chính. Đây là lịch đề xuất trong hồ sơ; kết quả duyệt chéo chưa có.

## 5. Khó khăn và cách xử lý

Chi phí token + tool không phản ánh đủ chi phí nhân viên; nhóm dùng CPS và chi phí cả hệ thống để đối chiếu. Cỡ mẫu theo cụm làm tăng nhu cầu tuyển nhân viên; pilot cần chốt thiết kế có đủ lực kiểm định. Các đầu việc dùng nhánh riêng và PR để phối hợp.

## 6. Tổng hợp đóng góp

Thao: code A–B, chỉ số và rủi ro. Dũng: kiểm số, bảng chi phí, code D1/E1. Bảo: phụ trách nhãn người 1, bảng khắc phục, pilot plan và phiếu chấm. Quảng: bộ nhãn người 2, hồ sơ launch và báo cáo nhóm. Bằng chứng chi tiết xem [TEAM.md](../../TEAM.md) và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Đo thời gian xem/làm lại thực tế thay các cột simulated; bổ sung đối chứng đồng thời và theo dõi lỗi ngầm bằng kiểm tra mẫu. Chỉ mở rộng khi đủ mẫu, chênh chỉ số chính ≥6 điểm %, cận dưới khoảng tin cậy 95% >0 và đạt luật dừng. Bổ sung kết quả duyệt chéo khi có bằng chứng.

## 8. Tài liệu tham khảo

[Đề bài lab](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [rubric](../../RUBRIC.md), [quy tắc](../../RULES.md), các hồ sơ liên kết ở trên.
