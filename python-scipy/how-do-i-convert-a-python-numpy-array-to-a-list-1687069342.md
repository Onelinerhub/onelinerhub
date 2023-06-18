# How do I convert a Python numpy array to a list?
// plain

The easiest way to convert a Python numpy array to a list is using the `tolist()` function. This function will convert the array to a list and return it.

## Example

```
import numpy as np

a = np.array([[1,2,3], [4,5,6]])

list_a = a.tolist()

print(list_a)
```
## Output example

```
[[1, 2, 3], [4, 5, 6]]
```

The `tolist()` function takes the array and converts it into a list of the same elements. The elements are grouped by their original position in the array.

## Code explanation

1. Importing the numpy library as np: `import numpy as np`
2. Creating the array: `a = np.array([[1,2,3], [4,5,6]])`
3. Converting the array to a list: `list_a = a.tolist()`
4. Printing the list: `print(list_a)`

## Helpful links
- [NumPy Documentation - tolist()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html)

onelinerhub: [How do I convert a Python numpy array to a list?](https://onelinerhub.com/python-scipy/how-do-i-convert-a-python-numpy-array-to-a-list-1687069342)