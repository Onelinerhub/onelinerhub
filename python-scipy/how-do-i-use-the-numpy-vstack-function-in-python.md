# How do I use the numpy vstack function in Python?
// plain

`np.vstack` is a function in the NumPy library used to stack arrays in sequence vertically (row wise). It takes a sequence of arrays of the same shape as arguments and returns a single array that is a concatenation of all of the input arrays.

## Example

```
import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

c = np.vstack((a,b))

print(c)
```
## Output example

```
[[1 2 3]
 [2 3 4]]
```

The code above uses the `np.vstack` function to stack two arrays `a` and `b` vertically. The output is a single array `c` that is the concatenation of `a` and `b`.

The parts of the code are as follows:

- `import numpy as np`: This imports the NumPy library as `np`, which provides access to the `vstack` function.

- `a = np.array([1, 2, 3])`: This creates an array `a` with elements `1, 2, 3`.

- `b = np.array([2, 3, 4])`: This creates an array `b` with elements `2, 3, 4`.

- `c = np.vstack((a,b))`: This uses the `np.vstack` function to stack `a` and `b` vertically.

- `print(c)`: This prints the output of the `np.vstack` function.

## Helpful links

- https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html
- https://www.geeksforgeeks.org/numpy-vstack-in-python/

onelinerhub: [How do I use the numpy vstack function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-numpy-vstack-function-in-python)