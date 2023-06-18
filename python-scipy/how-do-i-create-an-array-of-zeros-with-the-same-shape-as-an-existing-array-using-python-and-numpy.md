# How do I create an array of zeros with the same shape as an existing array using Python and NumPy?
// plain

Creating an array of zeros with the same shape as an existing array using Python and NumPy is easy. To do this, you can use the `np.zeros_like` function. This function takes an existing array and creates a new array filled with zeros that has the same shape as the existing array.

For example:
```
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

arr_zeros = np.zeros_like(arr)

print(arr_zeros)
```

## Output example

```
[[0 0 0]
 [0 0 0]]
```

The code above creates an array `arr` with shape `(2,3)` and then creates a new array `arr_zeros` with the same shape as `arr` filled with zeros.

## Code explanation


1. `import numpy as np`: Imports the NumPy library as `np`.
2. `arr = np.array([[1,2,3], [4,5,6]])`: Creates an array `arr` with shape `(2,3)`.
3. `arr_zeros = np.zeros_like(arr)`: Creates a new array `arr_zeros` with the same shape as `arr` filled with zeros.
4. `print(arr_zeros)`: Prints the new array.

## Helpful links
- [NumPy Documentation - np.zeros_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html)

onelinerhub: [How do I create an array of zeros with the same shape as an existing array using Python and NumPy?](https://onelinerhub.com/python-scipy/how-do-i-create-an-array-of-zeros-with-the-same-shape-as-an-existing-array-using-python-and-numpy)