# How do I join two arrays in Python using NumPy?
// plain

Joining two arrays in Python using NumPy is a fairly straightforward process. It can be done using the `np.concatenate()` function. This function takes a tuple or list of arrays to join together.

For example, if we have two NumPy arrays `a` and `b`, we can join them together using `np.concatenate()` like this:

```
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))

print(c)
```

The output of the above code would be:

```
[1 2 3 4 5 6]
```

The `np.concatenate()` function takes the following parameters:

- `tuple` or `list` of arrays to join together
- `axis`: The axis along which the arrays will be joined. If it is not specified, it defaults to 0.

## Code explanation


1. `import numpy as np`: Imports the NumPy library.
2. `a = np.array([1, 2, 3])`: Creates a NumPy array `a` with the values `[1, 2, 3]`.
3. `b = np.array([4, 5, 6])`: Creates a NumPy array `b` with the values `[4, 5, 6]`.
4. `c = np.concatenate((a, b))`: Joins the arrays `a` and `b` together using `np.concatenate()`.
5. `print(c)`: Prints the resulting array `c`.

## Helpful links

- [NumPy Documentation: np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)

onelinerhub: [How do I join two arrays in Python using NumPy?](https://onelinerhub.com/python-scipy/how-do-i-join-two-arrays-in-python-using-numpy)