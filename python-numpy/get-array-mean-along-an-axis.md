# Get array mean along an axis

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
mean = np.mean(arr,axis=1)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data
- `np.mean` - returns given array mean
- `axis=1` - returns array of mean values along horizontal axis (use `axis=0` to get mean values along vertical axis)

group: aggregates

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
mean = np.mean(arr,axis=1)
print(arr)
print(mean)
```
```
[[1 2]
 [3 4]]
[1.5 3.5]

```

