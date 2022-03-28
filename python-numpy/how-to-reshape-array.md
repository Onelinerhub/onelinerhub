# How to reshape Numpy array

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
rsp = arr.reshape(3,2)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1, 2, 3, 4, 5, 6]` - sample 1-dimensional array to use for reshaping
- `.reshape` - reshape given array to the specified dimensions
- `(3,2)` - rows/cols to reshape to (`2` columns and `3` rows in our case)
- `rsp` - contains reshaped array

group: shape

## Example: 
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
rsp = arr.reshape(3,2)
print(rsp)
```
```
[[1 2]
 [3 4]
 [5 6]]

```

