import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import place_poles
from scipy.integrate import solve_ivp

# Matriks A dan B
A = np.array([[0, 1],
              [0, -0.0018]])
B = np.array([[0],
              [493.3]])

# Posisi kutub yang diinginkan
desired_poles = np.array([-1, -2])

# Menghitung matriks gain feedback K
place_obj = place_poles(A, B, desired_poles)
K = place_obj.gain_matrix

print("Matriks Gain Feedback K:")
print(K)

# Matriks sistem tertutup
A_cl = A - B @ K

# Definisikan fungsi sistem tertutup
def closed_loop_system(t, x, A_cl):
    return A_cl @ x

# Kondisi awal
x0 = [1, 0]  # Misalkan posisi awal x1 = 1 dan x2 = 0

# Simulasi respon sistem tertutup
t_span = (0, 10)  # Rentang waktu simulasi dari 0 sampai 10 detik
t_eval = np.linspace(t_span[0], t_span[1], 500)  # Titik waktu evaluasi

# Lakukan integrasi numerik
sol = solve_ivp(closed_loop_system, t_span, x0, args=(A_cl,), t_eval=t_eval)

# Plot hasil simulasi
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[0], label='x1 (Position)')
plt.xlabel('Time (s)')
plt.ylabel('x1 (Position)')
plt.title('Closed-Loop System Response for x1')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(sol.t, sol.y[1], label='x2 (Velocity)')
plt.xlabel('Time (s)')
plt.ylabel('x2 (Velocity)')
plt.title('Closed-Loop System Response for x2')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
