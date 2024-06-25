import numpy as np
from scipy.signal import place_poles

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
