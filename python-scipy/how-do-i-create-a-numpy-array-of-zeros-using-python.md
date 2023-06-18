# How do I create a numpy array of zeros using Python?
// plain

Creating a numpy array of zeros using Python is very easy. The `numpy.zeros()` function can be used to create an array of zeros with a given shape. The syntax for this function is `numpy.zeros(shape, dtype=float, order='C')`. The `shape` parameter is a tuple that specifies the dimensions of the array. The `dtype` parameter is optional and can be used to specify the data type of the array. The `order` parameter can be used to specify whether the array should be stored in row-major (C-style) or column-major (Fortran-style) order.

## Example code

```
import numpy as np

# Create an array of zeros with shape (2,3)
a = np.zeros((2,3))

print(a)
```
## Output example

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

## Code explanation


* `import numpy as np`: This imports the `numpy` module and assigns it the alias `np`.
* `np.zeros((2,3))`: This creates an array of zeros with shape (2,3).
* `print(a)`: This prints the array to the screen.

## Helpful links

* [NumPy Documentation - zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)

onelinerhub: [How do I create a numpy array of zeros using Python?](https://onelinerhub.com/python-scipy/how-do-i-create-a-numpy-array-of-zeros-using-python)