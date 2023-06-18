# How do I convert a Python numpy.ndarray to a list?
// plain

To convert a Python numpy.ndarray to a list, you can use the `tolist()` method. This method will return a copy of the array data as a list.

For example:
```
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

list_arr = arr.tolist()

print(list_arr)
```

## Output example

```
[1, 2, 3, 4, 5]
```

The code above has the following parts:

1. `import numpy as np` - imports the numpy library and assigns it to the variable `np`
2. `arr = np.array([1, 2, 3, 4, 5])` - creates a numpy array with the values `1, 2, 3, 4, 5` and assigns it to the variable `arr`
3. `list_arr = arr.tolist()` - converts the numpy array in the variable `arr` to a list and assigns it to the variable `list_arr`
4. `print(list_arr)` - prints the list in the variable `list_arr`

## Helpful links
- [NumPy Array to List](https://www.geeksforgeeks.org/numpy-array-tolist-python/)
- [NumPy Tutorial](https://www.tutorialspoint.com/numpy/index.htm)

onelinerhub: [How do I convert a Python numpy.ndarray to a list?](https://onelinerhub.com/python-scipy/how-do-i-convert-a-python-numpy-ndarray-to-a-list)