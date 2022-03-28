import numpy as np
mtx = np.array([[1, 2], [3, 4], [5, 6]])
transposed = mtx.T  # transpose mtx
assert (transposed == np.array([[1, 3, 5], [2, 4, 6]])).all()
