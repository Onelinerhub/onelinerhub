# How can I use Python and NumPy to perform a XOR operation?
// plain

The XOR operation can be performed in Python using the NumPy library. The NumPy library has a logical_xor function which can be used to perform a XOR operation on two arrays.

The syntax for the logical_xor function is:
```
numpy.logical_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
```

Where x1 and x2 are the two arrays that will be used in the XOR operation.

For example:

```
import numpy as np

x1 = np.array([True, False, True])
x2 = np.array([True, True, False])

xor_result = np.logical_xor(x1, x2)

print(xor_result)
```

The output of the above code will be:
```
[False  True  True]
```

## Code explanation


- `import numpy as np` - This imports the NumPy library and assigns it the alias `np`.
- `x1 = np.array([True, False, True])` - This creates an array with the values `True`, `False`, and `True`.
- `x2 = np.array([True, True, False])` - This creates an array with the values `True`, `True`, and `False`.
- `xor_result = np.logical_xor(x1, x2)` - This uses the `logical_xor` function to perform a XOR operation on the two arrays `x1` and `x2`.
- `print(xor_result)` - This prints the result of the XOR operation.

## Helpful links

- [NumPy logical_xor](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_xor.html)

onelinerhub: [How can I use Python and NumPy to perform a XOR operation?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-numpy-to-perform-a-xor-operation)