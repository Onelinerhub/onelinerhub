# How can I create a Python Numpy array?
// plain

Creating a Python Numpy array is a simple process. To do this, you first need to import the Numpy module. This can be done with the following code:
```python
import numpy as np
```

Once the module is imported, you can create an array with the `np.array()` function. This function takes in a list or a tuple of elements and returns an array. For example:
```python
my_array = np.array([1, 2, 3, 4])
print(my_array)
```
Which will output:
```
[1 2 3 4]
```

You can also create an array of a certain size and populate it with a certain value using the `np.full()` function. This function takes in two parameters, the size of the array and the value to fill it with. For example:
```python
my_array = np.full((3, 3), 5)
print(my_array)
```
Which will output:
```
[[5 5 5]
 [5 5 5]
 [5 5 5]]
```

Finally, you can also create an array of a certain size and populate it with random numbers using the `np.random.random()` function. This function takes in the size of the array as a parameter. For example:
```python
my_array = np.random.random((3, 3))
print(my_array)
```
Which will output:
```
[[0.96450292 0.73732818 0.37096419]
 [0.89406676 0.83745894 0.91337229]
 [0.72300402 0.77236496 0.83626521]]
```

These are the main ways to create a Python Numpy array. For more information, you can refer to the [Numpy Documentation](https://numpy.org/doc/1.18/reference/generated/numpy.array.html).

onelinerhub: [How can I create a Python Numpy array?](https://onelinerhub.com/python-scipy/how-can-i-create-a-python-numpy-array)