# array

How do I use the Scipy asarray function in Python?
// plain

The `scipy.asarray` function is a convenient way to convert a Python sequence into a numpy array. This is useful when working with numerical data in Python, as it allows for faster processing and manipulation of data.

## Example code


```
import numpy as np
from scipy import asarray

my_list = [1, 2, 3]
np_array = asarray(my_list)

print(np_array)
```

## Output example

```
[1 2 3]
```

The code above creates a numpy array from a Python list. It does this by using the `scipy.asarray` function, which takes the list as an argument and returns a numpy array.

The code can be broken down into the following parts:

1. `import numpy as np`: This imports the numpy library, which is needed for creating and manipulating numpy arrays.

2. `from scipy import asarray`: This imports the `scipy.asarray` function from the scipy library.

3. `my_list = [1, 2, 3]`: This creates a Python list.

4. `np_array = asarray(my_list)`: This uses the `scipy.asarray` function to convert the Python list into a numpy array.

5. `print(np_array)`: This prints the numpy array to the console.

## Helpful links

- [Scipy Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.asarray.html)
- [Numpy Documentation](https://numpy.org/doc/stable/)

onelinerhub: [array

How do I use the Scipy asarray function in Python?](https://onelinerhub.com/python-scipy/array--how-do-i-use-the-scipy-asarray-function-in-python)