# How to calculate percentiles from Numpy array COPY

```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])

p10 = np.percentile(arr, 10)
p50 = np.percentile(arr, 50)
p95 = np.percentile(arr, 95)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.quantile` - calculate quantile of a given array on a given level
- `p10` - 10% percentile
- `p50` - 50% percentile (same as average)
- `p95` - 95% percentile

group: tiles

## Example: 
```python
import numpy as np
arr = np.array([1,2,3,6,7,8,10,11,12,15,16,17])
val = np.quantile(arr,.05)

p10 = np.percentile(arr, 10)
p50 = np.percentile(arr, 50)
p95 = np.percentile(arr, 95)

print('10%', p10)
print('50%', p50)
print('95%', p95)
```
```
10% 2.1
50% 9.0
95% 16.45

```

