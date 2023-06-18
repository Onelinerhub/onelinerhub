# How can I use the "where" function in Python Numpy?
// plain

The `where` function in Python Numpy can be used to return elements from an array based on a condition. It can be used in two different ways:

1. `np.where(condition, x, y)`: returns elements from x if the condition is true, and elements from y if the condition is false.

## Example


```
import numpy as np

array_1 = np.array([1, 2, 3, 4, 5])
array_2 = np.array([10, 20, 30, 40, 50])

# Return elements from array_1 if the element is greater than 3, else return elements from array_2
result = np.where(array_1 > 3, array_1, array_2)

print(result)
```
## Output example
 `[10 20 30  4  5]`


2. `np.where(condition)`: returns the indices of elements that satisfy the condition.

## Example


```
import numpy as np

array_1 = np.array([1, 2, 3, 4, 5])

# Return the indices of elements that are greater than 3
result = np.where(array_1 > 3)

print(result)
```
## Output example
 `(array([3, 4]),)`

## Helpful links
- [Numpy where function](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- [Numpy where function tutorial](https://www.geeksforgeeks.org/numpy-where-in-python/)

onelinerhub: [How can I use the "where" function in Python Numpy?](https://onelinerhub.com/python-scipy/how-can-i-use-the--where--function-in-python-numpy)