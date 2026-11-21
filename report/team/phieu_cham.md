# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): NhomCDEF (Lớp L3A)
- Nhóm được chấm: NhomTTBH (Lớp L3A · https://github.com/NguyenDacThe/K5-L3A-DAY13-NhomTTBH-LaunchEconomics)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất **Go có điều kiện** khớp số liệu, nêu đủ các con số bất lợi về kinh tế và cỡ mẫu (`quoc_te` 22.515 đ = 1,88×; xem lại 100% lên 11.743–12.415 đ = 0,98–1,03×; nửa khối lượng làm chi phí cố định tăng lên 2.370 đ/việc; power ≈ 0,64 ở mức +5 điểm, `simulated`) kèm cách xử lý và vai trò phụ trách cụ thể. Tại buổi duyệt chéo, Nhóm TTBH đã xác nhận bổ sung hai cổng chặn bắt buộc trước ngày khởi động `2026-12-07` (hoàn tất Mục 5 và kiểm tra bật đủ 13 event). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Gắn nhãn `simulated` đầy đủ trên mọi file hồ sơ, trạng thái `Giả lập` đúng cho Mục 1, 2, 3, 7; không dùng từ cấm và mỗi mục đều có một vai trò cụ thể phụ trách. Thu hẹp phạm vi về `noi_dia` (2.696 đ = 0,22×, thành công 95,0%) và `hang_nang` (8.221 đ = 0,69×, thành công 74,1%), loại `quoc_te` (22.515 đ = 1,88×, thành công 27,3%) và `doi_tac` (10.215 đ = 0,85×) có lý do bằng số rõ ràng. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | `pilot_plan.yaml` đọc hợp lệ bằng `yaml.safe_load` và không còn dấu `?`; chia ngẫu nhiên 20 + 20 nhân viên trên 12 depot, có đối chứng đồng thời và kiểm soát tràn tác động theo `staff_id`; tính đúng 5 câu D1 (`1.251`, `DE = 2,48`, `m ≥ 299`, `DE = 6,96`, `n` hiệu dụng `859`, nêu rõ power `0,642` ở +5 điểm); đủ 4 luật dừng chuẩn bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ dựa trên tỉ lệ mở lại thực tế `4,25%` (`3,97%` trong phạm vi), rollback 30 phút của Giám đốc vận hành. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ NhomTTBH đầy đủ bằng chứng định lượng, gắn nhãn `simulated` nhất quán, thu hẹp phạm vi hợp lý và thiết kế pilot tách được tác động kèm 4 luật dừng rõ ràng. Hội đồng duyệt **Go có điều kiện** với hai cổng chặn bắt buộc trước ngày khởi động `2026-12-07` đã được đội trình xác nhận bổ sung: hoàn tất Mục 5 (Bảng lỗi) và kiểm tra bật đủ 13 event đo thời gian thực tế.

**Một câu hỏi cho đội trình:** Mục 5 (Bảng lỗi) trong hồ sơ của nhóm đang ở trạng thái "Chưa" và mốc kiểm tra bật 13 event ghi phút thật đặt ngày `2026-12-14` (sau ngày chạy 1 tuần) — Nhóm TTBH có bổ sung hai điều kiện này thành cổng chặn bắt buộc trước ngày khởi động `2026-12-07` không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm TTBH xác nhận sẽ bổ sung hai điều kiện này thành cổng chặn bắt buộc trước ngày khởi động `2026-12-07`, cụ thể:
- Mục 5 (Bảng lỗi): Hoàn tất rà soát, cập nhật kết quả xử lý và xác nhận các lỗi ảnh hưởng đến việc khởi động đã được khắc phục trước khi chuyển trạng thái từ "Chưa" sang "Đã hoàn tất".
- 13 event: Điều chỉnh mốc kiểm tra từ ngày `2026-12-14` lên trước ngày `2026-12-07`; bảo đảm cả 13 event được bật và kiểm tra việc ghi nhận dữ liệu đầy đủ, đúng yêu cầu trước khi chạy.
Nhóm sẽ cập nhật hai điều kiện trên vào checklist và hồ sơ để làm căn cứ quyết định khởi động. Nếu một trong hai điều kiện chưa đạt, nhóm sẽ chưa triển khai và sẽ điều chỉnh lịch chạy phù hợp.
