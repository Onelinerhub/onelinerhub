# Get array mean along an axis

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
mean = np.mean(arr,axis=1)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data
- `np.mean(arr,axis=1)` - returns given array mean along the columns. i.e. mean of each row. Use `axis=0` to get mean along the rows i.e. mean of each column.

group: aggregates

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print( np.mean(arr,axis=1) )
```
```
2.5

```

