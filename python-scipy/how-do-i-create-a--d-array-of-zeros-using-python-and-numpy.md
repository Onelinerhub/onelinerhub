# How do I create a 2D array of zeros using Python and NumPy?
// plain

To create a 2D array of zeros using Python and NumPy, you can use the np.zeros() function. This function takes two arguments, the shape of the array (a tuple of integers) and the data type of the elements (optional).

For example, to create a 2x3 array of zeros, you can use the following code:

```
import numpy as np

arr = np.zeros((2,3))

print(arr)
```

The output of the code above will be:

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

The code contains the following parts:

- `import numpy as np`: imports the NumPy library and assigns it the alias ‘np’.
- `arr = np.zeros((2,3))`: creates a 2x3 array of zeros and assigns it to the variable ‘arr’.
- `print(arr)`: prints the contents of the array.

For more information, see the documentation for [np.zeros()](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html).

onelinerhub: [How do I create a 2D array of zeros using Python and NumPy?](https://onelinerhub.com/python-scipy/how-do-i-create-a--d-array-of-zeros-using-python-and-numpy)