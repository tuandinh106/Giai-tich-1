import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ==========================================
# 1. THU THẬP VÀ GIẢ ĐỊNH DỮ LIỆU (Mock Data)
# ==========================================
# Thời gian (tháng)
t_data = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
# Số lượng thiết bị IoT kết nối thực tế (giả định có nhiễu)
# Khởi điểm nhà có ít thiết bị, sau đó tăng mạnh, rồi từ từ bão hòa.
P_data = np.array([5, 7, 11, 20, 35, 60, 85, 110, 130, 142, 148, 151, 153])

# ==========================================
# 2. XÂY DỰNG MÔ HÌNH TOÁN HỌC (LOGISTIC)
# ==========================================
# Phương trình nghiệm của phương trình vi phân Logistic: P(t) = K / (1 + A * e^(-kt))
def logistic_model(t, K, A, k):
    return K / (1 + A * np.exp(-k * t))

# Sử dụng scipy.optimize.curve_fit để hồi quy tìm các hằng số K, A, k
# p0 là giá trị dự đoán ban đầu: [Ngưỡng max dự đoán, A dự đoán, tốc độ k dự đoán]
p0 = [160, 30, 0.3]
popt, pcov = curve_fit(logistic_model, t_data, P_data, p0=p0)

# Lấy các giá trị tối ưu vừa tìm được
K_opt, A_opt, k_opt = popt

# ==========================================
# 3. TÍNH TOÁN CÁC THÔNG SỐ GIẢI TÍCH 1
# ==========================================

# A. Giới hạn (Mục tiêu 3: Sức chịu tải tối đa)
# Theo Giải tích: lim (t->inf) P(t) = K
max_capacity = K_opt 

# B. Đạo hàm (Mục tiêu 2: Xác định điểm bùng phát)
# Hàm đạo hàm bậc 1: P'(t) = (K * A * k * e^(-kt)) / (1 + A * e^(-kt))^2
def growth_rate(t, K, A, k):
    numerator = K * A * k * np.exp(-k * t)
    denominator = (1 + A * np.exp(-k * t))**2
    return numerator / denominator

# Điểm bùng phát xảy ra khi P''(t) = 0. 
# Giải phương trình P''(t) = 0 ta được t = ln(A)/k
t_inflection = np.log(A_opt) / k_opt
P_inflection = logistic_model(t_inflection, K_opt, A_opt, k_opt) # Luôn bằng K/2
max_rate = growth_rate(t_inflection, K_opt, A_opt, k_opt)

# In kết quả ra màn hình
print("==== KẾT QUẢ PHÂN TÍCH MÔ HÌNH LOGISTIC ====")
print(f"1. Phương trình mô hình: P(t) = {K_opt:.2f} / (1 + {A_opt:.2f} * e^(-{k_opt:.4f}t))")
print(f"2. Ngưỡng bão hòa (K - Sức chịu tải tối đa): {max_capacity:.0f} thiết bị")
print(f"3. Thời điểm bùng phát (Điểm uốn): Tháng thứ {t_inflection:.2f}")
print(f"4. Số lượng thiết bị tại điểm bùng phát: {P_inflection:.0f} thiết bị (≈ K/2)")
print(f"5. Tốc độ kết nối cao nhất: {max_rate:.2f} thiết bị/tháng")

# ==========================================
# 4. VẼ ĐỒ THỊ TRỰC QUAN (MATPLOTLIB)
# ==========================================
t_fit = np.linspace(0, 30, 200) # Tạo mảng thời gian mượt mà từ 0 đến 30 tháng
P_fit = logistic_model(t_fit, K_opt, A_opt, k_opt)
rate_fit = growth_rate(t_fit, K_opt, A_opt, k_opt)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Đồ thị 1: Hàm P(t) - Quỹ đạo tăng trưởng
ax1.plot(t_data, P_data, 'ro', label='Dữ liệu thực tế giả định')
ax1.plot(t_fit, P_fit, 'b-', label='Đường cong Logistic hồi quy $P(t)$')
ax1.axhline(y=K_opt, color='g', linestyle='--', label=f'Ngưỡng bão hòa $K \\approx {K_opt:.0f}$')
# Đánh dấu điểm bùng phát
ax1.plot(t_inflection, P_inflection, 'k*', markersize=12, label=f'Điểm bùng phát (Tháng {t_inflection:.1f})')
ax1.set_title("Mô hình quỹ đạo tăng trưởng số lượng thiết bị IoT (Hàm P(t))", fontsize=14)
ax1.set_xlabel("Thời gian t (Tháng)")
ax1.set_ylabel("Số lượng thiết bị")
ax1.legend()
ax1.grid(True)

# Đồ thị 2: Hàm P'(t) - Tốc độ tăng trưởng
ax2.plot(t_fit, rate_fit, 'm-', label="Tốc độ tăng trưởng $P'(t)$")
ax2.axvline(x=t_inflection, color='k', linestyle='--', label=f'Thời điểm bùng phát (Tháng {t_inflection:.1f})')
ax2.plot(t_inflection, max_rate, 'r*', markersize=12, label=f'Tốc độ Max: {max_rate:.1f} tb/tháng')
ax2.set_title("Tốc độ gia tăng thiết bị mới theo thời gian (Hàm P'(t))", fontsize=14)
ax2.set_xlabel("Thời gian t (Tháng)")
ax2.set_ylabel("Tốc độ (Thiết bị / Tháng)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()