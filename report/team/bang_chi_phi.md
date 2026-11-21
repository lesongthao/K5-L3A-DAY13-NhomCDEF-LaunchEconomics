# Bảng chi phí · Nhiệm vụ A và B

**Nguồn:** Kết quả chạy `python lab13.py` trên `main` sau PR #1 do Dũng cung cấp; đầu vào `src/logix_runs.csv` (1.624 trace) và `src/logix_requests.csv` (1.200 yêu cầu). Đây là bộ dữ liệu giả lập của lab. Khoản dựa trên phút xem lại/làm lại mang nhãn **simulated**. Các số tiền làm tròn đến đồng theo đầu ra chương trình.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | **1,20** (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | **1,25** (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | **1,25** (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, mọi attempt | đo từ trace |
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv`, mọi attempt | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt > 1; **khoản nằm trong token + tool, không cộng thêm** | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| **Tổng chi phí** | **4.373.585** | tổng token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | **978** | `ket_qua == 'thanh_cong'` | dữ liệu giả lập của lab |
| **Chi phí mỗi việc thành công (CPS)** | **4.472** | 4.373.585 / 978 | simulated |
| Hóa đơn token và tool chia cho số yêu cầu | **274,7** | (245.585 + 84.000) / 1.200 | đo từ trace |

- **Chênh lệch:** CPS 4.472 đ gấp khoảng **16,3 lần** hóa đơn token + tool trên một yêu cầu (274,7 đ); không được coi tiền API là toàn bộ chi phí (simulated).
- **Khoản lớn nhất:** làm lại **2.264.000 đ = 51,8%**; tiếp theo xem lại **1.780.000 đ = 40,7%** tổng chi phí (simulated).
- **Đối chiếu toàn hệ thống:** 222 ca không thành công × 12.000 đ + 4.373.585 đ = **7.037.585 đ**, tức **5.865 đ/YC = 0,49 lần** baseline (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22x |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69x |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88x |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85x |

- **Không nên ưu tiên `quoc_te`:** CPS **22.515 đ**, vượt baseline **12.000 đ** 88%; thành công chỉ **27,3%** (simulated).
- **Chạy đến 3 lần không giải quyết được:** tỉ lệ `status == ok` của `quoc_te` giảm từ **30,0% → 11,4% → 2,2%** qua attempt 1–3; nên chuyển hướng xử lý hoặc giới hạn phạm vi pilot.

## A4 · Chi phí cố định (phạm vi `noi_dia` + `hang_nang`)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | **4.599 đ** (simulated) | 0,38x |
| Một nửa khối lượng (22.500/tháng) | 16.875 | 2.370 đ | **5.784 đ** (simulated) | 0,48x |

- **Chưa đổi kết luận** ở hai quy mô đề bài: CPS sau phân bổ cố định vẫn dưới **12.000 đ** (4.599 và 5.784 đ). Khi sản lượng giảm một nửa, phần cố định/việc tăng gấp đôi (simulated).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ / 1.000 token; tool giữ nguyên | **4.723 đ** (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ / 1.000 token | **4.346 đ** (simulated) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | **6.292 đ** (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | **3.562 đ** (simulated) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | **6.787 đ** (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | **3.315 đ** (simulated) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | **5.506 đ** (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Loại attempt > 2; cập nhật trạng thái không thành công | **4.237 đ** (simulated) | −5,2% |
| Chỉ cho chạy 1 lần | Chỉ giữ attempt 1; cập nhật trạng thái | **4.111 đ** (simulated) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- **Token × 2 + xem lại × 2:** CPS **6.543 đ** (**+46,3%**, simulated), cao hơn khi chỉ tăng một yếu tố.
- **Top 3 tác động tăng CPS:** 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1%), theo các kịch bản B1 (simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | **7.449.781 đ** (simulated) | **4.111 đ** (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | **6.901.220 đ** (simulated) | **4.237 đ** (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | **7.037.585 đ** (simulated) | **4.472 đ** (simulated) |

- **Cho công ty:** tối đa **2 lần** có tổng chi phí hệ thống thấp nhất (**6.901.220 đ**); không trùng giới hạn CPS thấp nhất là **1 lần** (**4.111 đ**), do tăng ca chuyển nhân viên (simulated).

## B4 · Nếu phải xem lại tất cả (`noi_dia` + `hang_nang`)

Đầu vào từ kết quả chạy: **948** ca xem lại, **5 phút/ca**; **48** ca làm lại; **900** việc thành công; token + tool **224.513 đ**. Chi phí nhân viên **2.000 đ/phút** (simulated).

| Cách tính thời gian làm lại | Tổng chi phí | CPS | So với 12.000 đ | Ngưỡng hòa vốn thời gian xem |
| --- | ---: | ---: | ---: | ---: |
| Giả định đề: **9 phút/ca** | **10.568.513 đ** (simulated) | **11.743 đ** (simulated) | **0,98x** | ≤ 5,1 phút |
| Trung bình dữ liệu: **≈15,3 phút/ca** | **11.173.054 đ** (simulated) | **12.415 đ** (simulated) | **1,03x** | ≤ 4,8 phút |

- **Kết luận:** nếu xem lại 100%, CPS có thể từ **11.743 đ** (dưới baseline) thành **12.415 đ** (vượt baseline) chỉ vì thời gian làm lại tăng từ **9** lên **≈15,3 phút** (simulated).
- **Pilot cần đo:** thời gian xem lại/làm lại **thực tế**, tỉ lệ phải sửa và chất lượng đầu ra; không thể chỉ dựa vào thời gian `simulated` để quyết định mở rộng.
