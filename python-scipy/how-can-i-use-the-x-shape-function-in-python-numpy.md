# How can I use the x.shape function in Python Numpy?
// plain

The `x.shape` function is a part of the NumPy library in Python and is used to find the shape of an array. It returns a tuple of the form `(rows, columns)`, where `rows` is the number of rows and `columns` is the number of columns in the array.

## Example


```
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

x.shape
```

## Output example


```
(3, 3)
```

The code above imports NumPy as `np` and creates an array `x` with three rows and three columns. Then the `x.shape` function is used to find the shape of the array `x`, which is `(3, 3)`.

## Code explanation

- `import numpy as np`: imports the NumPy library and assigns it to the alias `np`
- `np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`: creates an array `x` with three rows and three columns
- `x.shape`: finds the shape of the array `x`

## Helpful links
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy Shape Function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html)

onelinerhub: [How can I use the x.shape function in Python Numpy?](https://onelinerhub.com/python-scipy/how-can-i-use-the-x-shape-function-in-python-numpy)