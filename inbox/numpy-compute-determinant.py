import numpy as np
mtx = np.array([[1, 2], [3, 4]])
det = np.linalg.det(mtx)
print(f"{det} should be -2")
