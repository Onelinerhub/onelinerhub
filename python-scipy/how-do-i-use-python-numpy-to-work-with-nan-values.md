# How do I use Python Numpy to work with NaN values?
// plain

Python Numpy provides various functions to work with NaN values.

1. `np.nan_to_num()`: This function replaces NaN values with zero and Infinity values with finite numbers.

## Example

```
import numpy as np

arr = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])

print("Original array:")
print(arr)

temp = np.nan_to_num(arr)

print("\nAfter replacing NaN with zero:")
print(temp)
```
## Output example

```
Original array:
[nan  1.  2. nan  3.  4.  5.]

After replacing NaN with zero:
[0. 1. 2. 0. 3. 4. 5.]
```

2. `np.isnan()`: This function returns a boolean array of True and False values, where True corresponds to NaN values and False corresponds to non-NaN values.

## Example

```
import numpy as np

arr = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])

print("Original array:")
print(arr)

temp = np.isnan(arr)

print("\nBoolean array:")
print(temp)
```
## Output example

```
Original array:
[nan  1.  2. nan  3.  4.  5.]

Boolean array:
[ True False False  True False False False]
```

3. `np.where()`: This function returns indices of elements that satisfy a certain condition.

## Example

```
import numpy as np

arr = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])

print("Original array:")
print(arr)

temp = np.where(np.isnan(arr))

print("\nIndices of elements with value NaN:")
print(temp)
```
## Output example

```
Original array:
[nan  1.  2. nan  3.  4.  5.]

Indices of elements with value NaN:
(array([0, 3]),)
```

4. `np.fillna()`: This function is used to fill NaN values with some specified values.

## Example

```
import numpy as np

arr = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])

print("Original array:")
print(arr)

temp = np.fillna(arr, 0)

print("\nAfter replacing NaN with 0:")
print(temp)
```
## Output example

```
Original array:
[nan  1.  2. nan  3.  4.  5.]

After replacing NaN with 0:
[0. 1. 2. 0. 3. 4. 5.]
```

## Helpful links
- https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html
- https://numpy.org/doc/stable/reference/generated/numpy.isnan.html
- https://numpy.org/doc/stable/reference/generated/numpy.where.html
- https://numpy.org/doc/stable/reference/generated/numpy.fillna.html

onelinerhub: [How do I use Python Numpy to work with NaN values?](https://onelinerhub.com/python-scipy/how-do-i-use-python-numpy-to-work-with-nan-values)