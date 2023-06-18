# How do I create a Python numpy ndarray?
// plain

Creating a Python numpy ndarray is a simple process. To create one, you must first import the numpy library.

```python
import numpy as np
```

Then, you can create an array using the numpy.array() method. This method takes in a sequence of numbers or a list and creates a ndarray from it.

```python
# Create a numpy array from a sequence of numbers
my_array = np.array([1, 2, 3, 4])
print(my_array)
# Output: [1 2 3 4]

# Create a numpy array from a list
my_list = [5, 6, 7, 8]
my_array2 = np.array(my_list)
print(my_array2)
# Output: [5 6 7 8]
```

You can also create an array of a certain shape and type filled with zeros or ones by using the numpy.zeros() and numpy.ones() methods respectively.

```python
# Create an array of shape (2, 3) filled with zeros
my_array3 = np.zeros((2, 3))
print(my_array3)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# Create an array of shape (2, 3) filled with ones
my_array4 = np.ones((2, 3))
print(my_array4)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]]
```

Finally, you can also create an array filled with random numbers using the numpy.random.rand() method.

```python
# Create an array of shape (2, 3) filled with random numbers
my_array5 = np.random.rand(2, 3)
print(my_array5)
# Output:
# [[0.8018761  0.50878095 0.37440122]
#  [0.74143782 0.92293199 0.17585087]]
```

In summary, creating a numpy ndarray can be done using the numpy.array() method, numpy.zeros() and numpy.ones() methods, and the numpy.random.rand() method.

## Helpful links
- [Numpy Documentation](https://numpy.org/doc/)
- [Creating Numpy Arrays](https://www.datacamp.com/community/tutorials/creating-numpy-arrays)

onelinerhub: [How do I create a Python numpy ndarray?](https://onelinerhub.com/python-scipy/how-do-i-create-a-python-numpy-ndarray)