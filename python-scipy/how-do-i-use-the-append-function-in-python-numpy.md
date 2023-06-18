# How do I use the append function in Python Numpy?
// plain

The `append()` function in Python Numpy is used to combine two arrays. It takes in two parameters, the first being the array to which the other is appended. The second parameter is the array which is appended to the first. The `append()` function returns a new array with the two combined.

## Example

```
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = np.append(arr1, arr2)

print(arr3)
```
## Output example

```
[1 2 3 4 5 6]
```

The code above imports the Numpy library, then creates two arrays, `arr1` and `arr2`, and assigns them values. The `append()` function is then used to combine the two arrays, with `arr1` as the first parameter and `arr2` as the second. The `append()` function returns a new array, `arr3`, which is printed out.

Parts of the code:
- `import numpy as np`: imports the Numpy library
- `arr1 = np.array([1, 2, 3])`: creates an array called `arr1` and assigns it the values 1, 2, and 3
- `arr2 = np.array([4, 5, 6])`: creates an array called `arr2` and assigns it the values 4, 5, and 6
- `arr3 = np.array.append(arr1, arr2)`: uses the `append()` function to combine `arr1` and `arr2` into a new array called `arr3`
- `print(arr3)`: prints out the contents of `arr3`

## Helpful links
- [Numpy append() function documentation](https://numpy.org/doc/stable/reference/generated/numpy.append.html)
- [Python Numpy Tutorial](https://www.w3schools.com/python/numpy_intro.asp)

onelinerhub: [How do I use the append function in Python Numpy?](https://onelinerhub.com/python-scipy/how-do-i-use-the-append-function-in-python-numpy)