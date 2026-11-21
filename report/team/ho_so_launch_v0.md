# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: NhomCDEF · Lớp: L3A. Phạm vi quyết định: kế hoạch pilot. Nguồn: [chi phí](bang_chi_phi.md), [chỉ số/rủi ro](chi_so.md), [bảng lỗi](bang_loi.md), [pilot plan](pilot_plan.yaml). Chi phí có phần thời gian giả lập được ghi `simulated`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.373.585 đ / 978 việc = 4.472 đ/việc, gấp 16,3 lần hóa đơn token + tool/yêu cầu (simulated; A2). | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: 6.787 đ (+51,8%); xem lại ×2: 6.292 đ (+40,7%); lương +25%: 5.506 đ (+23,1%). Đổi riêng từng yếu tố (simulated; B1–B2). | Giả lập | Trưởng nhóm CSKH |
| 3 · So với nhân viên tự làm | Mốc tự làm 12.000 đ/yêu cầu. Cả hệ thống: 5.865 đ/yêu cầu = 0,49×, gồm xử lý 222 ca không thành công. CPS nội địa/hàng nặng/quốc tế/đối tác: 2.696/8.221/22.515/10.215 đ. Nội địa + hàng nặng cộng cố định: 4.599 đ ở 45.000 yêu cầu/tháng; 5.784 đ ở nửa khối lượng. Xem lại 100%: 11.743 đ (làm lại 9 phút), 12.415 đ (15,3 phút), có thể vượt mốc tự làm. Tất cả chi phí dẫn xuất trên: simulated (A2–A4, B4). | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, dùng, an toàn | Đợt chạy thử: đóng ≤24 giờ và không mở lại 7 ngày 82,83% (994/1.200); sửa/bỏ gợi ý 27,12% (48/177); mở lại 4,25% (51/1.200), trong phạm vi 3,97% (39/982; simulated theo pilot plan). Có 10 event với `trace_id` và đối chiếu cách tính; chưa có đối chứng để kết luận cải thiện (E1). | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và khắc phục | Đủ 20 ca và 5 phương án khắc phục đủ 5 loại, có phép đo và vai trò phụ trách. Bản Bảo cập nhật trùng nhãn gốc Quảng 16/20 = 80%; bốn ca lệch 4, 14, 15, 18 đã thống nhất. Chưa xác nhận quy trình độc lập; tỷ lệ này không chứng minh đồng thuận độc lập (C). | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Nội địa + hàng nặng, D01–D06; ngẫu nhiên theo nhân viên: 20 người/nhóm, ≥299 yêu cầu/người, 5.980 yêu cầu thực/nhóm, DE 6,96, ≈859 hiệu dụng. MDE 6 điểm %, alpha 0,05, power thiết kế 0,80; nếu hiệu ứng thật 5 điểm %, power chỉ 0,642. Rollout 10%→25%→50%, có 4 luật dừng và rollback 30 phút. Lịch đề xuất: bắt đầu 07/12/2026, quyết định 19/01/2027; cần xác nhận đủ 40 người (CSV chỉ có 20). | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2: CPS +51,8%; xem lại 100% có thể lên 12.415 đ/việc; nửa khối lượng làm cố định lên 2.370 đ/việc (simulated). Theo dõi làm lại >7%/tuần, CPS >8.000 đ trong 2 tuần, thời gian xem lại >5 phút và sản lượng <50% kế hoạch trong 2 tuần; xử lý theo E2 và luật dừng pilot. | Giả lập | PM trợ lý hoàn phí |

Điều kiện và mốc kiểm tra đề xuất (cần xác nhận trước khi chạy):

- **04/12/2026 — Kỹ sư trưởng agent:** xác minh tính độc lập của nhãn; nếu không xác minh được, giữ hạn chế và đánh giá mới trên ca chưa xem. Kiểm thử khắc phục 5 loại lỗi, chống hoàn trùng và thông báo ghi sổ.
- **04/12/2026 — Giám đốc vận hành LogiX-VN:** duyệt lịch, xác nhận đủ 40 người và lưu lượng ≥299 yêu cầu/người; thiếu thì trình lại thiết kế. Chấp nhận giới hạn power 0,642 với hiệu ứng thật 5 điểm %.
- **07/12/2026 — Kế toán trưởng:** xác nhận đo thật thời gian xem/làm lại và đối soát giao dịch trước khởi động; chưa đo được thì chưa chạy.
- **Từ 07/12/2026 — Giám đốc vận hành LogiX-VN:** thực thi 4 luật dừng trong pilot plan, rollback 30 phút khi có sự cố an toàn. **14/12/2026 và hằng tuần — PM trợ lý hoàn phí:** rà chi phí/sản lượng; CPS >8.000 đ hai tuần thì dừng đợt đo, trình lại phạm vi.
- **19/01/2027 — Giám đốc vận hành LogiX-VN:** chỉ đề xuất mở rộng nếu đủ mẫu và theo dõi 7 ngày, chênh ≥6 điểm %, cận dưới CI 95% >0, đạt an toàn/chi phí/sử dụng. Thiếu mẫu thì giữ phạm vi và chốt lại lịch trước khi đọc chỉ số chính.

**Đề xuất: Go có điều kiện** cho kế hoạch pilot nội địa + hàng nặng tại D01–D06, với các điều kiện, vai trò và ngày kiểm tra nêu trên.
