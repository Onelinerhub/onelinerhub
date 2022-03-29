# How to calculate 1st quartile from Numpy array

```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])

val = np.percentile(arr, 25)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.percentile` - calculate percentile of a given array on a given level
- `val` - will contain 1st quartile (25% percentile)

group: tiles

## Example: 
```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])

val = np.percentile(arr, 25)

print(val)
```
```
5.25

```

