# How do I use Python Scipy to calculate a QR decomposition?
// plain

The QR decomposition is the factorization of a matrix into an orthogonal matrix and an upper triangular matrix. To calculate a QR decomposition in Python Scipy, the `scipy.linalg.qr` function can be used.

```
import scipy
import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
Q, R = scipy.linalg.qr(A)
print(Q)
print(R)
```

## Output example

```
[[-0.12309149  0.90453403  0.40824829]
 [-0.49236596  0.30151134 -0.81649658]
 [-0.86164044 -0.30151134  0.40824829]]
[[-8.12403840e+00 -9.60113630e+00 -1.10782342e+01]
 [ 0.00000000e+00  9.04534034e-01  1.80906807e+00]
 [ 0.00000000e+00  0.00000000e+00 -1.11164740e-15]]
```

The `scipy.linalg.qr` function takes the matrix `A` as an argument and returns two matrices, `Q` and `R`. `Q` is an orthogonal matrix, and `R` is an upper triangular matrix. In the example code, the matrix `A` is a 3x3 matrix, and the output is two 3x3 matrices.

Parts of the code:
- `import scipy`: imports the scipy library
- `import numpy as np`: imports the numpy library with the alias `np`
- `A = np.array([[1,2,3],[4,5,6],[7,8,9]])`: creates a 3x3 matrix `A`
- `Q, R = scipy.linalg.qr(A)`: calculates the QR decomposition of `A` and assigns the orthogonal matrix `Q` to the variable `Q` and the upper triangular matrix `R` to the variable `R`
- `print(Q)`: prints the matrix `Q`
- `print(R)`: prints the matrix `R`

## Helpful links
- [Scipy QR Decomposition Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr.html)
- [Numpy Array Documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)

onelinerhub: [How do I use Python Scipy to calculate a QR decomposition?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-calculate-a-qr-decomposition)