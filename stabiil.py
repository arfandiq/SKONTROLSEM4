import numpy as np

A_cl = np.array([[0, 1],
                 [-2.000264089, -2.998087672]])

# Hitung eigenvalues
eigvals = np.linalg.eigvals(A_cl)

print("Eigenvalues dari matriks A - BK:")
print(eigvals)
