# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Nguồn ca lỗi: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục “Hai mươi ca lỗi”. Nhãn dựa trên nguyên nhân gốc và dấu hiệu phát hiện trong từng ca.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Bảo (@BaoAIuet), bản gắn nhãn có hỗ trợ của Codex, chờ Bảo xác nhận. Người gắn nhãn 2: Quảng (@nbquang04), chờ nộp nhãn gốc.

| Ca | Nhãn gốc người 1 | Nhãn gốc người 2 | Trùng | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | — | — | — |
| 2 | Hệ thống | — | — | — |
| 3 | Ngữ cảnh | — | — | — |
| 4 | Giới hạn hệ thống | — | — | — |
| 5 | Ngầm | — | — | — |
| 6 | Do người dùng | — | — | — |
| 7 | Hệ thống | — | — | — |
| 8 | Hệ thống | — | — | — |
| 9 | Do người dùng | — | — | — |
| 10 | Ngữ cảnh | — | — | — |
| 11 | Giới hạn hệ thống | — | — | — |
| 12 | Ngầm | — | — | — |
| 13 | Giới hạn hệ thống | — | — | — |
| 14 | Do người dùng | — | — | — |
| 15 | Hệ thống | — | — | — |
| 16 | Ngữ cảnh | — | — | — |
| 17 | Ngầm | — | — | — |
| 18 | Ngữ cảnh | — | — | — |
| 19 | Giới hạn hệ thống | — | — | — |
| 20 | Hệ thống | — | — | — |

**Tỉ lệ đồng thuận** sẽ được tính bằng số ca trùng / 20 × 100% ngay khi có nhãn gốc của cả hai người. Mốc đạt là 16/20 ca.

## Quy tắc phân biệt cho các ca không trùng

Chờ đối chiếu. Với mỗi ca lệch, ghi một câu giải thích tiêu chí chọn nhãn. Nếu dưới 16/20, nhóm làm rõ định nghĩa trước khi chốt.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Theo dõi `refund_account_validation_failed` theo ngân hàng mỗi ngày, ngưỡng cảnh báo là có ít nhất 1 lệnh bị ngân hàng trả vì thiếu chữ số. | Kiểm tra định dạng theo ngân hàng trước khi tạo lệnh và cho khách xác nhận lại tài khoản đã che bớt số. | PM luồng hoàn phí |
| 7 | Hệ thống | Đối chiếu thông báo thành công với giao dịch ghi sổ theo `trace_id` theo thời gian thực. Cảnh báo ngay khi có 1 thông báo thành công thiếu giao dịch đã ghi sổ. | Chỉ gửi thông báo thành công sau khi xác nhận ghi sổ. Nếu hết lượt thử, chuyển nhân viên và báo trạng thái đang xử lý. | Kỹ sư phụ trách tích hợp sổ cái |
| 3 | Ngữ cảnh | Mỗi tuần đếm số yêu cầu mở lại trong 7 ngày với lý do chờ tiền về ngân hàng sau khi đã hoàn vào ví. Rà soát nội dung khi có từ 2 ca. | Hiển thị đích nhận tiền là ví LogiX trước khi xác nhận và nhắc lại đích nhận cùng thời gian dự kiến trong thông báo. | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Đếm `unsupported_input` với `input_type=audio` mỗi tuần. Kiểm tra ngay khi có 1 ca thiếu hướng dẫn nhập chữ hoặc chuyển nhân viên. | Với tin nhắn thoại, gửi hướng dẫn chuyển sang văn bản và cung cấp luồng chuyển nhân viên nếu khách cần hỗ trợ. | PM kênh hỗ trợ |
| 17 | Ngầm | Mỗi tuần đối soát tối đa 100 đơn dưới 2 kg đã hoàn với bảng giá có hiệu lực tại thời điểm áp dụng. Cảnh báo khi có ít nhất 1 đơn lệch. | Xóa bộ nhớ đệm khi bảng giá đổi, ghi phiên bản bảng giá theo `trace_id` và rà lại các đơn đã dùng phiên bản cũ. | Kế toán trưởng |
