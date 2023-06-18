# How do I convert a Python Numpy array to a list?
// plain

The easiest way to convert a Python Numpy array to a list is to use the `tolist()` method. This method will convert the Numpy array into a list, and return the list.

For example, let's create a Numpy array:
```
import numpy as np

arr = np.array([1,2,3,4])
```

Now, let's convert it to a list:
```
list_arr = arr.tolist()

print(list_arr)
```

## Output example

```
[1, 2, 3, 4]
```

The `tolist()` method is a built-in method of the Numpy library, and it takes no arguments.

Additionally, if you just want to iterate over the elements of the Numpy array, you can use the `for` loop syntax, as follows:
```
for elem in arr:
    print(elem)
```

## Output example

```
1
2
3
4
```

## Helpful links
- [Numpy Documentation: ndarray.tolist](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html)
- [Real Python: How to Iterate Through a Numpy Array](https://realpython.com/iterate-through-numpy-array/)

onelinerhub: [How do I convert a Python Numpy array to a list?](https://onelinerhub.com/python-scipy/how-do-i-convert-a-python-numpy-array-to-a-list)