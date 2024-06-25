import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definisikan fungsi sistem tertutup
def closed_loop_system(t, x, A_cl):
    return A_cl @ x

# Matriks sistem tertutup
A_cl = np.array([[0, 1],
                 [-2.000264089, -2.998087672]])

# Kondisi awal
x0 = [1, 0]  # Misalkan posisi awal x1 = 1 dan x2 = 0

# Simulasi respon sistem tertutup
t_span = (0, 10)  # Rentang waktu simulasi dari 0 sampai 10 detik
t_eval = np.linspace(t_span[0], t_span[1], 500)  # Titik waktu evaluasi

# Lakukan integrasi numerik
sol = solve_ivp(closed_loop_system, t_span, x0, args=(A_cl,), t_eval=t_eval)

# Plot hasil simulasi
plt.plot(sol.t, sol.y[0], label='x1 (Position)')
plt.plot(sol.t, sol.y[1], label='x2 (Velocity)')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Closed-Loop System Response')
plt.legend()
plt.grid()
plt.show()
