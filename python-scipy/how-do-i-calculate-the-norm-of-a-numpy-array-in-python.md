# How do I calculate the norm of a numpy array in Python?
// plain

The norm of a numpy array is the length of the array, which can be calculated using the `numpy.linalg.norm()` function.

```
import numpy as np

arr = np.array([1, 2, 3])

norm = np.linalg.norm(arr)

print(norm)
```

## Output example

```
3.7416573867739413
```

The code above:

- `import numpy as np`: imports the numpy library into the script
- `arr = np.array([1, 2, 3])`: creates a numpy array from the list of numbers
- `norm = np.linalg.norm(arr)`: calculates the norm of the numpy array
- `print(norm)`: prints the result

## Helpful links
- [Numpy linalg.norm() documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html)
- [Calculating the Euclidean Norm of a Vector](https://www.mathsisfun.com/algebra/vectors-norm.html)

onelinerhub: [How do I calculate the norm of a numpy array in Python?](https://onelinerhub.com/python-scipy/how-do-i-calculate-the-norm-of-a-numpy-array-in-python)