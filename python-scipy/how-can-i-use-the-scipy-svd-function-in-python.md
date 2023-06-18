# How can I use the SciPy SVD function in Python?
// plain

The SciPy SVD function allows you to decompose a matrix into its constituent parts using Singular Value Decomposition (SVD).

To use the SciPy SVD function in Python, you simply need to import the `scipy.linalg` module and call the `svd` function. For example:

```
import numpy as np
from scipy.linalg import svd

A = np.array([[1,2],[3,4],[5,6]])
U, s, VT = svd(A)

print(U)
print(s)
print(VT)
```

## Output example

```
[[-0.2298477   0.88346102  0.40824829]
 [-0.52474482  0.24078249 -0.81649658]
 [-0.81964194 -0.40189603  0.40824829]]
[9.52551809 0.51430058]
[[-0.61962948 -0.78489445]
 [-0.78489445  0.61962948]]
```

The code consists of the following parts:

1. Import the `scipy.linalg` module: `import numpy as np` and `from scipy.linalg import svd`.
2. Create a matrix `A`: `A = np.array([[1,2],[3,4],[5,6]])`.
3. Call the `svd` function: `U, s, VT = svd(A)`.
4. Print the results: `print(U)`, `print(s)`, and `print(VT)`.

For more information about the SciPy SVD function, see the [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html).

onelinerhub: [How can I use the SciPy SVD function in Python?](https://onelinerhub.com/python-scipy/how-can-i-use-the-scipy-svd-function-in-python)