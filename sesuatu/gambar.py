import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)  # Biar konsisten

# Banyak titik
n_points = 200
t = np.linspace(0, 1, n_points)

# ------------------------------------------------
# 1) GROUND TRUTH (LURUS)
#    Misal robot jalan lurus sepanjang 10 meter
# ------------------------------------------------
x_gt = 10 * t
y_gt = np.zeros_like(t)  # lurus di y = 0

# ------------------------------------------------
# 2) ODOMETRY BAGUS (NOISE KECIL)
# ------------------------------------------------
noise_odom_x = np.random.normal(0, 0.03, size=n_points)
noise_odom_y = np.random.normal(0, 0.03, size=n_points)

x_odom = x_gt + noise_odom_x
y_odom = y_gt + noise_odom_y

# ------------------------------------------------
# 3) GPS: awalnya bagus -> loncat -> bagus lagi
# ------------------------------------------------
# Dasarnya: GT + noise kecil
noise_gps_x = np.random.normal(0, 0.15, size=n_points)
noise_gps_y = np.random.normal(0, 0.15, size=n_points)

x_gps = x_gt + noise_gps_x
y_gps = y_gt + noise_gps_y

# Segment loncat (misal antara 30%–50% lintasan)
start_jump = int(0.30 * n_points)
end_jump   = int(0.50 * n_points)

# Offset loncat GPS (misal geser 3m di X dan 2m di Y)
jump_dx = 3.0
jump_dy = 2.0

x_gps[start_jump:end_jump] += jump_dx
y_gps[start_jump:end_jump] += jump_dy

# ------------------------------------------------
# PLOT
# ------------------------------------------------
plt.figure(figsize=(8, 5))

# Ground truth: garis halus
plt.plot(x_gt, y_gt, label='Ground Truth', linewidth=2)

# Odometry bagus: point cloud mepet
plt.scatter(x_odom, y_odom, s=15, label='Odometry Bagus', alpha=0.8)

# GPS: point cloud, kelihatan ada loncatan
plt.scatter(x_gps, y_gps, s=20, marker='x', label='GPS', alpha=0.8)

# Tandai area loncatan dengan shading (opsional)
plt.axvspan(x_gt[start_jump], x_gt[end_jump-1],
            alpha=0.1, label='Periode GPS Jump')

plt.title('Ground Truth vs Odometry Bagus vs GPS (dengan Jump)')
plt.xlabel('X (meter)')
plt.ylabel('Y (meter)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
