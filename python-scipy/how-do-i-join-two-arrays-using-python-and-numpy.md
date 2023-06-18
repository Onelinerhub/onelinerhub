# How do I join two arrays using Python and NumPy?
// plain

Joining two arrays using Python and NumPy is done using the `np.concatenate()` function. It takes a sequence of arrays and combines them into a single array.

## Example code

```
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)
```
## Output example
 `[1 2 3 4 5 6]`

The code above contains the following parts:
1. `import numpy as np` imports the NumPy library into the program.
2. `a = np.array([1, 2, 3])` and `b = np.array([4, 5, 6])` create two NumPy arrays.
3. `np.concatenate((a, b))` joins the two arrays into a single array.
4. `print(c)` prints the result of the concatenation.

## Helpful links
- https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
- https://www.geeksforgeeks.org/numpy-concatenate-python/

onelinerhub: [How do I join two arrays using Python and NumPy?](https://onelinerhub.com/python-scipy/how-do-i-join-two-arrays-using-python-and-numpy)