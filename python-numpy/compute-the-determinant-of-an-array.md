# Compute the determinant of an array

```python
import numpy as np
mtx = np.array([[1, 2], [3, 4]])
det = np.linalg.det(mtx)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data
- `np.linalg.det` - returns determinant of a given matric
- `mtx` - name of the matrix to get determinant of

## Example: 
```python
import numpy as np
mtx = np.array([[1, 2], [3, 4]])
det = np.linalg.det(mtx)
print(det)
```
```
-2.0000000000000004

```

