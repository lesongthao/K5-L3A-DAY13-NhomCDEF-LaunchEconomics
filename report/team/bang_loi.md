# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Nguồn ca lỗi: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục “Hai mươi ca lỗi”. Nhãn dựa trên nguyên nhân gốc và dấu hiệu phát hiện trong từng ca.

## Đối chiếu hai bộ nhãn

Người gắn nhãn 1: Bảo (@BaoAIuet). Người gắn nhãn 2: Quảng (@nbquang04).

| Ca | Nhãn người 1 (Bảo) | Nhãn người 2 (Quảng) | Trùng (Bảo–Quảng) | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Do người dùng | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Hệ thống | Do người dùng | Không | Do người dùng |
| 15 | Ngữ cảnh | Hệ thống | Không | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 16/20 = 80%.

## Quy tắc phân biệt cho các ca không trùng

Bảo chọn áp dụng nhãn Quảng đã nộp cho bốn ca lệch, dựa trên các căn cứ sau.

- **Ca 4 — Giới hạn hệ thống:** LogiX thiếu dữ liệu chặng do hãng nước ngoài giao, nên trợ lý chuyển yêu cầu cho nhân viên.
- **Ca 14 — Do người dùng:** Khách bấm nhầm nút xác nhận đã nhận tiền, khiến yêu cầu bị đóng.
- **Ca 15 — Hệ thống:** Trợ lý tính hoàn 100% thay vì 50% theo chính sách. Nhân viên phát hiện sai lệch ở bước xem lại.
- **Ca 18 — Ngữ cảnh:** Trợ lý hoàn đúng 15.000 đ. Khách hiểu là hoàn thiếu vì thông báo chưa giải thích cách tính.

## Ghi chú cho các ca dễ nhầm

- Ca 6 và 9 bắt đầu từ việc khách chọn sai mục hoặc nhập sai mã.
- Ca 12 có kết quả đúng nhưng chi phí tăng gấp ba mà chưa được phát hiện.
- Ca 13 nằm ngoài phạm vi hoàn phí mà trợ lý xử lý.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Theo dõi `refund_account_validation_failed` theo ngân hàng mỗi ngày, ngưỡng cảnh báo là có ít nhất 1 lệnh bị ngân hàng trả vì thiếu chữ số. | Kiểm tra định dạng theo ngân hàng trước khi tạo lệnh và cho khách xác nhận lại tài khoản đã che bớt số. | PM luồng hoàn phí |
| 7 | Hệ thống | Đối chiếu thông báo thành công với giao dịch ghi sổ theo `trace_id` theo thời gian thực. Cảnh báo ngay khi có 1 thông báo thành công thiếu giao dịch đã ghi sổ. | Chỉ gửi thông báo thành công sau khi xác nhận ghi sổ. Nếu hết lượt thử, chuyển nhân viên và báo trạng thái đang xử lý. | Kỹ sư phụ trách tích hợp sổ cái |
| 3 | Ngữ cảnh | Mỗi tuần đếm số yêu cầu mở lại trong 7 ngày với lý do chờ tiền về ngân hàng sau khi đã hoàn vào ví. Rà soát nội dung khi có từ 2 ca. | Hiển thị đích nhận tiền là ví LogiX trước khi xác nhận và nhắc lại đích nhận cùng thời gian dự kiến trong thông báo. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Đếm `unsupported_input` với `input_type=audio` mỗi tuần. Kiểm tra ngay khi có 1 ca thiếu hướng dẫn nhập chữ hoặc chuyển nhân viên. | Với tin nhắn thoại, gửi hướng dẫn chuyển sang văn bản và cung cấp luồng chuyển nhân viên nếu khách cần hỗ trợ. | PM kênh hỗ trợ |
| 17 | Ngầm | Mỗi tuần đối soát tối đa 100 đơn dưới 2 kg đã hoàn với bảng giá có hiệu lực tại thời điểm áp dụng. Cảnh báo khi có ít nhất 1 đơn lệch. | Xóa bộ nhớ đệm khi bảng giá đổi, ghi phiên bản bảng giá theo `trace_id` và rà lại các đơn đã dùng phiên bản cũ. | Kế toán trưởng |
