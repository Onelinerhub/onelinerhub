# How to copy Numpy array

```python
import numpy as np

arr = np.array([1, 2, 3])
arr_copy = np.copy(arr)
```

- `np.array` - declare Numpy array
- `.copy` - copy specified array
- `arr` - array to copy
- `arr_copy` - copy of `arr` array

## Example: 
```python
import numpy as np

arr = np.array([1, 2, 3])
arr_copy = np.copy(arr)

arr[1] = 10
print(arr[1])

print(arr_copy[1])
```
```
10
2

```

