# How do I create a zero matrix using Python and Numpy?
// plain

Creating a zero matrix using Python and Numpy is a common operation. To do this, first import the numpy library.

```python
import numpy as np
```

Then, use the `np.zeros` function to create a zero matrix. This function takes a single argument which is a tuple that specifies the shape of the matrix. For example, to create a 3x4 matrix, the following code can be used:

```python
zero_matrix = np.zeros((3, 4))
print(zero_matrix)
```

## Output example

```
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
```

The code consists of the following parts:
* `import numpy as np` imports the numpy library and assigns it the alias `np`
* `np.zeros` creates a matrix filled with zeros. It takes a single argument which is a tuple that specifies the shape of the matrix
* `print(zero_matrix)` prints the created matrix

## Helpful links
* [Numpy Documentation](https://numpy.org/doc/)
* [Numpy zeros function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)

onelinerhub: [How do I create a zero matrix using Python and Numpy?](https://onelinerhub.com/python-scipy/how-do-i-create-a-zero-matrix-using-python-and-numpy)