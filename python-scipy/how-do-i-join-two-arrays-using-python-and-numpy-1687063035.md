# How do I join two arrays using Python and NumPy?
// plain

Joining two arrays using Python and NumPy can be done in several ways, depending on the desired result. One way is to use the np.concatenate() function. This function takes in an iterable of arrays and returns a single array with the elements from each array in the order they were provided.

For example:
```
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr_joined = np.concatenate((arr1, arr2))
print(arr_joined)
```

## Output example

```
[1 2 3 4 5 6]
```

The code above uses the np.concatenate() function to join two arrays, arr1 and arr2. The np.concatenate() function takes in an iterable of arrays and returns a single array with the elements from each array in the order they were provided. The output is a single array, arr_joined, containing the elements of arr1 and arr2 in the order they were provided.

Other ways of joining two arrays include using np.stack(), np.vstack(), and np.hstack().

## Helpful links
- [NumPy concatenate() Function](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)
- [NumPy stack() Function](https://numpy.org/doc/stable/reference/generated/numpy.stack.html)
- [NumPy vstack() Function](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)
- [NumPy hstack() Function](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html)

onelinerhub: [How do I join two arrays using Python and NumPy?](https://onelinerhub.com/python-scipy/how-do-i-join-two-arrays-using-python-and-numpy-1687063035)