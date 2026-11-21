"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python lab13.py   (cần pandas; Nhiệm vụ D sẽ cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập. Bản gốc nằm ở lab13_starter.py.
"""
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO, GIA_RA, GIA_TOOL = 26, 130, 15  # đồng: /1.000 token vào, /1.000 token ra, /lần gọi tool
LUONG_PHUT, BASELINE = 2000, 12000      # đồng: /phút nhân viên, 1 yêu cầu tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000            # đồng/tháng chi phí cố định của trợ lý
SAN_LUONG_THANG = 45_000                # yêu cầu/tháng ở quy mô đầy đủ


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def _kiem_tra_tham_so_a1(p: float, k: int | None) -> None:
    """Kiểm tra xác suất p trong (0, 1] và số lần chạy tối đa k (>= 1 hoặc None)."""
    if not (0.0 < p <= 1.0):
        raise ValueError(f'Xác suất p phải thuộc (0, 1], nhận được {p}.')
    if k is not None and k < 1:
        raise ValueError(f'Số lần chạy tối đa k phải >= 1 hoặc None, nhận được {k}.')


def so_lan_chay_ky_vong(p: float, k: int | None = None) -> float:
    """Tính số lần chạy trung bình cho 1 yêu cầu (tham số p: xác suất đúng, k: giới hạn lần chạy; trả về float)."""
    _kiem_tra_tham_so_a1(p, k)
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p: float, k: int | None = None) -> float:
    """Tính xác suất thành công sau tối đa k lần chạy (tham số p: xác suất đúng, k: giới hạn; trả về float)."""
    _kiem_tra_tham_so_a1(p, k)
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p: float, k: int | None = None) -> float:
    """Tính bội số chi phí mỗi việc thành công (tham số p: xác suất đúng, k: giới hạn; trả về float)."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc() -> None:
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu (không tham số, không trả về)."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(
    runs: pd.DataFrame,
    reqs: pd.DataFrame,
    gia_vao: float = GIA_VAO,
    gia_ra: float = GIA_RA,
    gia_tool: float = GIA_TOOL,
    luong_phut: float = LUONG_PHUT,
    he_so_xem_lai: float = 1.0,
    he_so_lam_lai: float = 1.0,
    max_lan_chay: int | None = None,
) -> dict[str, float]:
    """Tính mô hình chi phí mỗi việc thành công (CPS) từ dữ liệu trace.

    Tham số: runs (bảng lần chạy), reqs (bảng yêu cầu), đơn giá/hệ số (độ nhạy), max_lan_chay (giới hạn chạy lại).
    Trả về: dict gồm token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    """
    if len(reqs) == 0:
        raise ValueError('Bảng yêu cầu không được rỗng.')
    reqs_bs = reqs.copy()
    runs_loc = runs[runs['request_id'].isin(reqs_bs['request_id'])].copy()

    # Nếu có giới hạn chạy lại: loại attempt vượt ngưỡng và chuyển nhân viên làm thay
    if max_lan_chay is not None:
        if max_lan_chay < 1:
            raise ValueError(f'max_lan_chay phải >= 1, nhận được {max_lan_chay}.')
        runs_loc = runs_loc[runs_loc['attempt'] <= max_lan_chay]
        vuot = reqs_bs['so_lan_chay'] > max_lan_chay
        reqs_bs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs_bs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số cộng mọi lần chạy kể cả lần lỗi; chia 1.000 vì đơn giá tính trên 1.000 token
    tien_token = runs_loc['tokens_in'] / 1000.0 * gia_vao + runs_loc['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs_loc['tool_calls'] * gia_tool
    chay_lai = float((tien_token + tien_tool)[runs_loc['attempt'] > 1].sum())
    xem_lai = float(reqs_bs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs_bs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai)

    token_tong, tool_tong = float(tien_token.sum()), float(tien_tool.sum())
    tong = token_tong + tool_tong + xem_lai + lam_lai
    thanh_cong = int((reqs_bs['ket_qua'] == 'thanh_cong').sum())
    if thanh_cong == 0:
        raise ValueError('Không có yêu cầu nào đạt thanh_cong để tính CPS.')

    return {
        'token': token_tong,
        'tool': tool_tong,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': float(thanh_cong),
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': (token_tong + tool_tong) / len(reqs_bs),
    }


def in_nhiem_vu_a(runs: pd.DataFrame, reqs: pd.DataFrame) -> dict[str, float]:
    """Tính và in bảng Nhiệm vụ A (A2, A3, A4) từ runs và reqs; trả về dict kết quả gốc A2."""
    kq = mo_hinh(runs, reqs)
    khong_tc = len(reqs) - int(kq['thanh_cong'])
    he_thong_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)

    print('\n=== NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    print(f"Token (mọi lần chạy)             : {kq['token']:>10,.0f} đ  [đo từ trace]")
    print(f"Tool ({int(runs['tool_calls'].sum()):,} lần gọi)            : {kq['tool']:>10,.0f} đ  [đo từ trace]")
    print(f"  - Phần lần chạy 2 và 3         : {kq['chay_lai']:>10,.0f} đ  [đo từ trace]")
    print(f"Xem lại ({int(reqs['phut_xem_lai_simulated'].sum()):,} phút)              : {kq['xem_lai']:>10,.0f} đ  [simulated]")
    print(f"Làm lại ({int(reqs['phut_lam_lai_simulated'].sum()):,} phút)            : {kq['lam_lai']:>10,.0f} đ  [simulated]")
    print(f"Tổng chi phí                     : {kq['tong']:>10,.0f} đ  [có phần simulated]")
    print(f"Số việc thành công               : {kq['thanh_cong']:>10,.0f}")
    print(f"Chi phí mỗi việc thành công (CPS): {kq['cps']:>10,.0f} đ  [simulated]")
    print(f"Hoá đơn token+tool / yêu cầu     : {kq['hoa_don_moi_yc']:>10,.1f} đ  [đo từ trace]")
    print(f"-> CPS gấp {kq['cps']/kq['hoa_don_moi_yc']:.1f}x hoá đơn; làm lại {kq['lam_lai']/kq['tong']*100:.1f}% [simulated], "
          f"xem lại {kq['xem_lai']/kq['tong']*100:.1f}% [simulated].")
    print(f"-> Cả hệ thống/YC (cộng {khong_tc} ca không thành công * 12k): {he_thong_yc:,.0f} đ = {he_thong_yc/BASELINE:.2f}x [simulated].")

    print('\n=== NHIỆM VỤ A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f"{'Loại':<10} {'Số YC':>6} {'Thành công':>11} {'Lần chạy/YC':>12} {'CPS [sim]':>12} {'So 12.000đ':>11}")
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        sub_reqs = reqs[reqs['loai'] == loai]
        sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        kq_l = mo_hinh(sub_runs, sub_reqs)
        print(f"{loai:<10} {len(sub_reqs):>6d} {kq_l['thanh_cong']/len(sub_reqs)*100:>10.1f}% "
              f"{len(sub_runs)/len(sub_reqs):>12.2f} {kq_l['cps']:>10,.0f} đ {kq_l['cps']/BASELINE:>10.2f}x")

    # Tỉ lệ lần chạy ok theo từng attempt để chứng minh quoc_te chạy lại không hiệu quả
    pivot_ok = (runs.assign(ok=(runs['status'] == 'ok').astype(float))
                .merge(reqs[['request_id', 'loai']], on='request_id')
                .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100.0)
    print('\nTỉ lệ status == ok theo lần thử (%):\n' + pivot_ok.loc[['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']].round(1).to_string())

    print('\n=== NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    ti_le_pv = kq_pv['thanh_cong'] / len(reqs)
    for nhan, hs in (('45.000 yc/tháng', 1.0), ('Nửa khối lượng (22.500 yc/tháng)', 0.5)):
        viec_thang = SAN_LUONG_THANG * hs * ti_le_pv
        co_dinh = CHI_PHI_CO_DINH / viec_thang
        tong_cps = kq_pv['cps'] + co_dinh
        print(f"- {nhan:<32}: {viec_thang:>7,.0f} việc | cố định {co_dinh:>5,.0f} đ | tổng {tong_cps:>5,.0f} đ ({tong_cps/BASELINE:.2f}x) [simulated]")
    return kq


def in_nhiem_vu_b(runs: pd.DataFrame, reqs: pd.DataFrame, cps_goc: float) -> None:
    """Tính và in bảng độ nhạy Nhiệm vụ B (B1, B2, B3, B4) dựa trên runs, reqs và cps_goc."""
    kich_ban: list[tuple[str, dict[str, float | int]]] = [
        ('Giá token gấp đôi', {'gia_vao': 52, 'gia_ra': 260}),
        ('Giá token giảm một nửa', {'gia_vao': 13, 'gia_ra': 65}),
        ('Tỉ lệ xem lại gấp đôi', {'he_so_xem_lai': 2.0}),
        ('Tỉ lệ xem lại giảm một nửa', {'he_so_xem_lai': 0.5}),
        ('Số ca làm lại gấp đôi', {'he_so_lam_lai': 2.0}),
        ('Số ca làm lại giảm một nửa', {'he_so_lam_lai': 0.5}),
        ('Lương nhân viên tăng 25%', {'luong_phut': 2500}),
        ('Chỉ cho chạy tối đa 2 lần', {'max_lan_chay': 2}),
        ('Chỉ cho chạy 1 lần', {'max_lan_chay': 1}),
    ]
    print('\n=== NHIỆM VỤ B1 & B2 · ĐỘ NHẠY CHI PHÍ ===')
    kq_b1: dict[str, float] = {}
    for ten, ts in kich_ban:
        cps = mo_hinh(runs, reqs, **ts)['cps']
        pct = (cps / cps_goc - 1.0) * 100.0
        kq_b1[ten] = pct
        print(f"{ten:<28}: {cps:>8,.0f} đ [simulated] ({pct:+6.1f}%)")

    # Kiểm chứng tính tuyến tính: giảm nửa phải đối xứng đúng một nửa mức tăng gấp đôi
    for tx2, tnua in (('Giá token gấp đôi', 'Giá token giảm một nửa'),
                      ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
                      ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa')):
        assert abs(kq_b1[tnua] + kq_b1[tx2] / 2.0) < 1e-9

    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"Đổi cặp (Token x2 + Xem lại x2): {cps_cap:,.0f} đ [simulated] ({(cps_cap/cps_goc - 1)*100:+.1f}%)")
    print('Top 3 yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên')

    print('\n=== NHIỆM VỤ B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG ===')
    print(f"{'Giới hạn':<10} {'Tổng trợ lý [sim]':>18} {'Không TC':>9} {'Cả hệ thống [sim]':>18} {'CPS [sim]':>11}")
    for gh in (1, 2, 3):
        kq_g = mo_hinh(runs, reqs, max_lan_chay=gh)
        khong_tc = len(reqs) - int(kq_g['thanh_cong'])
        print(f"{gh} lần      {kq_g['tong']:>16,.0f} đ {khong_tc:>9d} {kq_g['tong'] + khong_tc * BASELINE:>16,.0f} đ {kq_g['cps']:>9,.0f} đ")

    print('\n=== NHIỆM VỤ B4 · XEM LẠI 100% (noi_dia + hang_nang) ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    id_ok = set(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'])
    so_xem, so_lam = int(pv['request_id'].isin(id_ok).sum()), int((pv['ket_qua'] == 'lam_lai').sum())
    so_tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    tien_tt = float((runs_pv['tokens_in'] / 1000.0 * GIA_VAO + runs_pv['tokens_out'] / 1000.0 * GIA_RA + runs_pv['tool_calls'] * GIA_TOOL).sum())
    phut_lam_tb = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    print(f"Đầu vào: {so_xem} ca xem lại (5 phút/lần), {so_lam} ca làm lại, {so_tc} việc TC, token+tool {tien_tt:,.0f} đ")

    for nhan, phut_lam in (('Giả định đề (9.0 phút/ca)', 9.0), (f'Trung bình dữ liệu ({phut_lam_tb:.1f} phút/ca)', phut_lam_tb)):
        tien_lam = so_lam * phut_lam * LUONG_PHUT
        tong_b4 = tien_tt + so_xem * 5.0 * LUONG_PHUT + tien_lam
        cps_b4 = tong_b4 / so_tc
        hoa_von = (BASELINE * so_tc - tien_tt - tien_lam) / (so_xem * LUONG_PHUT)
        print(f"- {nhan}: tổng {tong_b4:,.0f} đ -> CPS {cps_b4:,.0f} đ = {cps_b4/BASELINE:.2f}x [simulated] (hòa vốn xem <= {hoa_von:.1f} phút)")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    kq_a2 = in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs, kq_a2['cps'])
    # TODO CP4 · Nhiệm vụ D & E1 (TV2 bổ sung sau khi gộp PR #1).
