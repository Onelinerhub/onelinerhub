# How do I use the NumPy transpose function in Python?
// plain

The NumPy transpose function is used to transpose a given array in Python. Transposing an array means to exchange the rows and columns of the array. It can be used by passing the array into the transpose() function.

```
import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print("Original array:")
print(arr)

transposed_arr = np.transpose(arr)

print("Transposed array:")
print(transposed_arr)
```

## Output example

```
Original array:
[[1 2 3]
 [4 5 6]]
Transposed array:
[[1 4]
 [2 5]
 [3 6]]
```

The code above consists of the following parts:
- import numpy as np: imports the NumPy library into the program.
- arr = np.array([[1,2,3], [4,5,6]]): creates an array with two rows and three columns.
- print("Original array:"): prints the text "Original array:" to the console.
- print(arr): prints the original array to the console.
- transposed_arr = np.transpose(arr): transposes the array.
- print("Transposed array:"): prints the text "Transposed array:" to the console.
- print(transposed_arr): prints the transposed array to the console.

## Helpful links
- https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
- https://www.geeksforgeeks.org/numpy-transpose-python/

onelinerhub: [How do I use the NumPy transpose function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-numpy-transpose-function-in-python)