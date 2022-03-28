# How to flatten multi-dimensional Numpy array

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
f = a.flatten()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data (2-dimensional array)
- `.flatten()` - returns flat 1-dimensional array from given multi-dimensional array

## Example: 
```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a.flatten())
```
```
[1 2 3 4]

```

