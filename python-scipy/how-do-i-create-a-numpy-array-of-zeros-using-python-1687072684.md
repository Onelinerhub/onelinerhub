# How do I create a numpy array of zeros using Python?
// plain

Creating a numpy array of zeros using Python is simple. To do this, the `numpy` library must be imported.

```python
import numpy as np
```

Then, a numpy array can be created using the `zeros` function, passing in the desired shape of the array as an argument. For example, to create an array of zeros with a shape of (2,3):

```python
arr = np.zeros((2,3))

print(arr)
```

## Output example

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

The code can be broken down as follows:
1. `import numpy as np` imports the `numpy` library, and assigns it the alias `np` for easy access.
2. `arr = np.zeros((2,3))` creates a numpy array of zeros with a shape of (2,3) and assigns it to the variable `arr`.
3. `print(arr)` prints the array to the console.

For more information, see the [Numpy Documentation](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html).

onelinerhub: [How do I create a numpy array of zeros using Python?](https://onelinerhub.com/python-scipy/how-do-i-create-a-numpy-array-of-zeros-using-python-1687072684)