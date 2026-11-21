# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai == 1`) | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) · phạm vi `noi_dia` + `hang_nang`: **3,97%** (39/982) |
| Dùng (tự đề xuất) | Tỉ lệ áp dụng trợ lý ở nhóm can thiệp | Số yêu cầu phạm vi `noi_dia` + `hang_nang` của nhóm can thiệp có `agent_suggestion_shown`, chia tổng số yêu cầu thuộc phạm vi của nhóm can thiệp | Không cần tính |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (lỗi ngầm) | Số đơn có `so_tien_da_hoan != so_tien_dung`, chia tổng số đơn được kế toán kiểm tra mẫu (100 đơn/tuần) | Không cần tính |

Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200), không kết luận trợ lý đã nâng chỉ số từ mức nền 0,70 vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Danh sách gồm 10 event, mọi event đều gắn `trace_id` để nối với trace của trợ lý.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm`, `staff_id`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý hoàn phí | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiện lên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất xử lý lại ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý hoàn phí | `reason`, `tom_tat`, `so_lan_thu`, `trace_id` | Khi trợ lý dừng và chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `handled_by`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu đã đóng |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Hằng tuần khi kiểm tra mẫu 100 đơn |

**Kiểm tra chéo:** mọi chỉ số trong bảng E1 đều tính được trực tiếp từ danh sách event ở trên:

- **% đóng trong 24 giờ và không mở lại trong 7 ngày (Chính):** ghép `refund_request_created` (`created_at`, `arm`), `ticket_closed` (`closed_at <= created_at + 24h`) và không tồn tại `ticket_reopened` trong vòng 7 ngày sau `closed_at` theo cùng `trace_id`.
- **Tỉ lệ bỏ qua gợi ý (Dùng):** đếm `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số bản ghi `staff_review_decision` có trong kỳ.
- **Tỉ lệ lỗi lọt đến khách (An toàn):** đếm số `trace_id` phát sinh `ticket_reopened` trong vòng 7 ngày kể từ `ticket_closed`, chia tổng số `refund_request_created` theo từng `arm`.
- **Tỉ lệ áp dụng trợ lý ở nhóm can thiệp (Dùng — tự đề xuất):** đếm số `trace_id` có `agent_suggestion_shown`, chia số `refund_request_created` thuộc `arm = treatment` và `loai` nằm trong `noi_dia`, `hang_nang`.
- **Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu (An toàn — tự đề xuất):** đếm bản ghi `audit_sample_checked` có `lech_tien != 0`, chia tổng số bản ghi `audit_sample_checked` trong tuần.
- **Đo chi phí thật thay thế cột giả lập:** ghép `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`), `staff_review_decision` (`phut_xem_lai` đo thật) và `staff_rework_completed` (`phut_lam_lai` đo thật) theo `trace_id`.

## E2 · Rủi ro kinh tế

Số liệu tác động lấy trực tiếp từ kết quả chạy `src/lab13.py` cho Nhiệm vụ A4, B1 và B4; mọi chi phí có sử dụng cột thời gian nhân viên giả lập đều ghi nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng **+51,8%**, từ 4.472 đ lên **6.787 đ/việc** (`simulated`, bảng B1) | Tỉ lệ làm lại hằng tuần trong phạm vi `noi_dia` + `hang_nang` > **7,0%** (mức chạy thử: 4,89%, 48/982 ca) hoặc CPS > **8.000 đ** trong 2 tuần liên tiếp | Thu hẹp pilot về riêng `noi_dia`, giới hạn tối đa 2 lần chạy và rà soát 20 trace làm lại để sửa lỗi gốc | PM trợ lý hoàn phí |
| Duy trì xem lại 100% kéo dài | Trong phạm vi `noi_dia` + `hang_nang`, CPS lên **11.743 đ = 0,98×** (mốc làm lại 9,0 phút/ca) hoặc **12.415 đ = 1,03×** (trung bình dữ liệu 15,3 phút/ca) so với 12.000 đ (`simulated`, bảng B4); mức hòa vốn đòi hỏi xem lại ≤ **5,1 phút/ca** (mốc 9 phút) hoặc ≤ **4,8 phút/ca** (mốc 15,3 phút) | Tỉ lệ yêu cầu phải xem lại vẫn > **50%** cuối bước rollout 0,25 hoặc thời gian xem lại đo thật > **5 phút/ca** | Giảm tỉ lệ xem lại theo bậc cho `noi_dia` khi tỉ lệ `sua + bo` < **15%** trong 1 tuần liên tiếp; rút gọn giao diện gợi ý để giảm thời gian xem lại dưới 4,5 phút | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn kế hoạch làm chi phí cố định tăng mạnh | Chi phí cố định 40 triệu đ/tháng là **1.185 đ/việc** ở quy mô 45.000 yêu cầu/tháng (33.750 việc thành công phạm vi `noi_dia` + `hang_nang`, tổng CPS **4.599 đ = 0,38×**, `simulated`, A4), tăng gấp đôi lên **2.370 đ/việc** nếu khối lượng còn một nửa (16.875 việc/tháng, tổng CPS **5.784 đ = 0,48×**, `simulated`, A4) | Số việc thành công hằng tuần < **50%** kế hoạch của bước rollout hiện tại trong 2 tuần liên tiếp | Tạm dừng mở rộng sang bước rollout tiếp theo, rà soát nguyên nhân nhân viên ít mở trợ lý và đàm phán lại gói vận hành cố định | PM trợ lý hoàn phí |
