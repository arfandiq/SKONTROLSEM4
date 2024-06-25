import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, lsim

# Definisikan parameter sistem kontrolable
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([1, 0])
D = np.array([0])

# Tentukan kestabilan sistem dengan eigenvalue
eigenvalues, _ = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)

# Periksa controlability
Co = np.hstack((B, A @ B))
if np.linalg.matrix_rank(Co) == len(A):
    print("System is controllable")
else:
    print("System is not controllable")
    raise ValueError("System is not controllable, pole placement cannot be applied")

# Spesifikasi desain kontrol
desired_poles = np.array([-2, -3])  # Tentukan posisi pole yang diinginkan

# Menggunakan scipy untuk menghitung feedback gain
K = scipy.linalg.place_poles(A, B, desired_poles).gain_matrix
print("Feedback gain K:", K)

# Definisikan sistem dengan feedback
A_cl = A - B @ K

# Buat sistem state-space closed-loop
sys_cl = StateSpace(A_cl, B, C, D)

# Simulasi respons sistem
t = np.linspace(0, 10, 500)  # Waktu simulasi
u = np.ones_like(t)  # Setpoint
x0 = np.array([0, 0])  # Kondisi awal

t, y, x = lsim(sys_cl, U=u, T=t, X0=x0)

# Plot grafik respons
plt.figure()
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Output')
plt.title('Closed-Loop System Response')
plt.grid()
plt.show()
