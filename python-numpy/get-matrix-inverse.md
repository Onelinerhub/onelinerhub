# Calculate matrix inverse

```python
import numpy as np
mtx = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(mtx)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `[[1, 2], [3, 4]]` - sample matrix data (2-dimensional array)
- `.linalg.inv(` - returns inverse (multiplicative) matrix for the given one 
- `inv` - will contain inverse matrix

group: matrix

## Example: 
```python
import numpy as np
mtx = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(mtx)
print(inv)
```
```
[[-2.   1. ]
 [ 1.5 -0.5]]

```

