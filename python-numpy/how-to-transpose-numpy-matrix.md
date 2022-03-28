# How to transpose Numpy matrix

```python
import numpy as np
mtx = np.array([[1, 2], [3, 4], [5, 6]])
transposed = mtx.T
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.T` - returns transposed matrix from the specified one

## Example: 
```python
import numpy as np
mtx = np.array([[1, 2], [3, 4], [5, 6]])
transposed = mtx.T  # transpose mtx
print(transposed)
```
```
[[1 3 5]
 [2 4 6]]

```

