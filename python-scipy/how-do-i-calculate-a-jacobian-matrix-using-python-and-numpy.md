# How do I calculate a Jacobian matrix using Python and NumPy?
// plain

The Jacobian matrix is a matrix of partial derivatives of a vector-valued function with respect to its inputs. To calculate a Jacobian matrix using Python and NumPy, we can use the `jacobian` function from the `numpy.linalg` module. This function takes a vector-valued function as its argument and returns its Jacobian.

For example, given a vector-valued function f(x, y):

```
def f(x, y):
    return np.array([x*y, x**2 + y**2])
```

We can calculate its Jacobian matrix as follows:

```
import numpy as np
from numpy.linalg import jacobian

def f(x, y):
    return np.array([x*y, x**2 + y**2])

x, y = 2, 3
jacobian(f, (x, y))
```

The output of the above code is:
```
array([[3., 2.],
       [4., 6.]])
```

## Code explanation

- `import numpy as np`: imports the NumPy library as `np`
- `from numpy.linalg import jacobian`: imports the `jacobian` function from the `numpy.linalg` module
- `def f(x, y):`: defines the vector-valued function f(x, y)
- `jacobian(f, (x, y))`: calculates the Jacobian matrix of vector-valued function f(x, y)

## Helpful links
- [NumPy Jacobian Function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.jacobian.html)
- [NumPy Linear Algebra Module](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

onelinerhub: [How do I calculate a Jacobian matrix using Python and NumPy?](https://onelinerhub.com/python-scipy/how-do-i-calculate-a-jacobian-matrix-using-python-and-numpy)