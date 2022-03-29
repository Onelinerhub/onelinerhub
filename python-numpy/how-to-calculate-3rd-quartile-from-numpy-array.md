# How to calculate 3rd quartile from Numpy array

```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])

val = np.percentile(arr, 75)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.percentile` - calculate percentile of a given array on a given level
- `val` - will contain 3rd quartile (75% percentile)

group: tiles

## Example: 
```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])

val = np.percentile(arr, 75)

print(val)
```
```
12.75

```

