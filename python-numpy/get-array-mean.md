# Get array mean

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
mean = np.mean(arr)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data
- `np.mean` - returns given array mean

group: aggregates

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print( np.mean(arr) )
```
```
2.5

```

