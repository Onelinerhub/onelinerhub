# How do I calculate the cross-correlation of two arrays using Python and NumPy?
// plain

To calculate the cross-correlation of two arrays using Python and NumPy, the `np.correlate()` function can be used. This function computes the correlation as a discrete linear convolution of two one-dimensional sequences.

## Example code

```
import numpy as np
a = np.array([1, 2, 3])
b = np.array([0, 1, 0.5])
np.correlate(a, b, 'full')
```
## Output example

```
array([0.5, 2. , 3.5, 2. , 0.5])
```

## Code explanation

- `import numpy as np`: imports the NumPy library as np
- `a = np.array([1, 2, 3])`: creates an array a with the values 1, 2, 3
- `b = np.array([0, 1, 0.5])`: creates an array b with the values 0, 1, 0.5
- `np.correlate(a, b, 'full')`: calculates the cross-correlation of the arrays a and b with the full option, which returns the entire cross-correlation sequence

## Helpful links
- [NumPy Cross-Correlation Documentation](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html)
- [NumPy Array Documentation](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

onelinerhub: [How do I calculate the cross-correlation of two arrays using Python and NumPy?](https://onelinerhub.com/python-scipy/how-do-i-calculate-the-cross-correlation-of-two-arrays-using-python-and-numpy)