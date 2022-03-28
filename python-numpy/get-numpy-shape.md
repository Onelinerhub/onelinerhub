# Get Numpy array shape

```python
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6]])
shp = arr.shape
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1, 2, 3, 4, 5, 6]` - sample 1-dimensional array to use for reshaping
- `.shape` - attribute returns shape of given array

group: shape

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6]])
shp = arr.shape
print(shp)
```
```
(3, 2)

```

