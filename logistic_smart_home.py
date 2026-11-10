import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = ['Arial', 'Segoe UI', 'Tahoma', 'sans-serif']

t_data = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
P_data = np.array([5, 7, 11, 20, 35, 60, 85, 110, 130, 142, 148, 151, 153])

def logistic_model(t, K, A, k):
    return K / (1 + A * np.exp(-k * t))

def growth_rate(t, K, A, k):
    return (K * A * k * np.exp(-k * t)) / (1 + A * np.exp(-k * t))**2

p0 = [160, 30, 0.3]
popt, _ = curve_fit(logistic_model, t_data, P_data, p0=p0, 
                    bounds=([0, 0, 0], [np.inf, np.inf, np.inf]), maxfev=20000)
K_opt, A_opt, k_opt = popt

max_capacity = K_opt
t_inflection = np.log(A_opt) / k_opt
P_inflection = logistic_model(t_inflection, K_opt, A_opt, k_opt)
max_rate = growth_rate(t_inflection, K_opt, A_opt, k_opt)

P_pred = logistic_model(t_data, K_opt, A_opt, k_opt)
ss_res = np.sum((P_data - P_pred) ** 2)
ss_tot = np.sum((P_data - np.mean(P_data)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

t_fit = np.linspace(0, 30, 300)
P_fit = logistic_model(t_fit, K_opt, A_opt, k_opt)
rate_fit = growth_rate(t_fit, K_opt, A_opt, k_opt)

fig = plt.figure(figsize=(14, 8))
fig.suptitle("PHÂN TÍCH TOÁN HỌC: MÔ HÌNH LOGISTIC TRONG SMART HOME", fontsize=18, fontweight='bold', color='#1f2a44')
gs = gridspec.GridSpec(2, 2, width_ratios=[2.5, 1])

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(t_data, P_data, 'ko', markersize=6, label='Dữ liệu giả định/nội suy')
ax1.plot(t_fit, P_fit, 'b-', linewidth=2.5, label='Đường cong Logistic $P(t)$')
ax1.axhline(y=K_opt, color='r', linestyle='--', alpha=0.7)

ax1.annotate(f'Ngưỡng bão hòa số thiết bị: $K \\approx {K_opt:.0f}$', 
             xy=(25, K_opt), xytext=(15, K_opt - 30),
             arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
             fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1.5))

ax1.set_title("1. Quỹ đạo tích lũy thiết bị IoT theo thời gian", fontsize=12, fontweight='bold')
ax1.set_ylabel("Số lượng thiết bị", fontsize=11)
ax1.set_xlabel("Thời gian (Tháng)", fontsize=11)
ax1.legend(loc='lower right')

ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
ax2.fill_between(t_fit, rate_fit, color='#a0c4ff', alpha=0.5)
ax2.plot(t_fit, rate_fit, color='#004aad', linewidth=2.5, label="$P'(t)$ (Đạo hàm bậc 1)")

ax2.plot(t_inflection, max_rate, 'r*', markersize=12)
ax2.axvline(x=t_inflection, color='k', linestyle=':', alpha=0.6)
ax2.annotate(f'ĐIỂM BÙNG PHÁT\n$P\'\'(t)=0$ (Tháng {t_inflection:.1f})', 
             xy=(t_inflection, max_rate), xytext=(t_inflection + 2, max_rate - 2),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="#ffcc00", ec="black", lw=1))

ax2.set_title("2. Tốc độ kết nối mới (Vận tốc tăng trưởng)", fontsize=12, fontweight='bold')
ax2.set_xlabel("Thời gian (Tháng)", fontsize=11)
ax2.set_ylabel("Thiết bị / Tháng", fontsize=11)
ax2.legend(loc='upper right')

ax3 = fig.add_subplot(gs[:, 1])
ax3.axis('off')

info_text = (
    "TỔNG HỢP THÔNG SỐ TOÁN HỌC\n"
    "--------------------------------------\n\n"
    "1. Phương trình mô hình:\n"
    f"$P(t) = \\frac{{{K_opt:.1f}}}{{1 + {A_opt:.2f}e^{{-{k_opt:.3f}t}}}}$\n\n"
    "2. Đánh giá mô hình:\n"
    f"Hệ số xác định $R^2$ = {r_squared:.4f}\n"
    "(>0.95: Mô hình rất khớp dữ liệu)\n\n"
    "3. Giới hạn (Khảo sát dài hạn):\n"
    f"$\\lim_{{t \\to \\infty}} P(t) = K = {max_capacity:.0f}$ (thiết bị)\n"
    "-> Ngưỡng số thiết bị theo kịch bản mô hình\n\n"
    "4. Phân tích Đạo hàm:\n"
    f"- Thời điểm bùng phát: Tháng {t_inflection:.1f}\n"
    f"- Tốc độ tối đa: {max_rate:.1f} (thiết bị/tháng)\n"
    f"- Khối lượng lúc đó: $P = K/2 = {P_inflection:.0f}$"
)

bbox_props = dict(boxstyle="round,pad=1.8", fc="#f8f9fa", ec="#ced4da", lw=2)
ax3.text(0.15, 0.5, info_text, fontsize=12.5, verticalalignment='center', 
         bbox=bbox_props, linespacing=1.9)

plt.tight_layout()
plt.show()