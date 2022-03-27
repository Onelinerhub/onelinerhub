# Get array average

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
average = np.average(arr)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data
- `np.average` - returns given array average

group: aggregates

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print( np.average(arr) )
```
```
2.5

```

