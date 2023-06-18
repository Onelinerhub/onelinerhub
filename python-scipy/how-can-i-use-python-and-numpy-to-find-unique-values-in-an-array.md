# How can I use Python and NumPy to find unique values in an array?
// plain

Using Python and NumPy, you can find unique values in an array by using the `np.unique()` function. This function takes an array as an argument and returns a sorted array of unique values in the array. For example:

```python
import numpy as np

arr = np.array([1, 2, 3, 3, 4, 4, 5])

unique_vals = np.unique(arr)

print(unique_vals)
```

This will output:
```
[1 2 3 4 5]
```

The `np.unique()` function works by looping through the given array and adding each value to a set. Since sets only contain unique values, each value will only be added once. After all values have been added to the set, the set is then converted into an array and sorted.

The parts of the code above are:
1. `import numpy as np` - imports the NumPy library and assigns it to the `np` alias.
2. `arr = np.array([1, 2, 3, 3, 4, 4, 5])` - creates a NumPy array with the given values.
3. `unique_vals = np.unique(arr)` - calls the `np.unique()` function and assigns the returned array to the `unique_vals` variable.
4. `print(unique_vals)` - prints the `unique_vals` array.

## Helpful links
- [NumPy Documentation - np.unique()](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)

onelinerhub: [How can I use Python and NumPy to find unique values in an array?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-numpy-to-find-unique-values-in-an-array)