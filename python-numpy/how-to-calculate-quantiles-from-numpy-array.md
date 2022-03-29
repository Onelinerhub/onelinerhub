# How to calculate quantile from Numpy array

```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])

q10 = np.quantile(arr,.10)
q50 = np.quantile(arr,.5)
q95 = np.quantile(arr,.95)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.quantile` - calculate quantile of a given array on a given level
- `q10` - 0.1 quanile
- `q50` - 0.5 quantile (same as average)
- `q95` - 0.95 quantile

group: tiles

## Example: 
```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])
val = np.quantile(arr,.05)

q10 = np.quantile(arr,.10)
q50 = np.quantile(arr,.5)
q95 = np.quantile(arr,.95)

print('10%', q10)
print('50%', q50)
print('95%', q95)
```
```
10% 2.1
50% 9.0 9.0
95% 16.45

```

