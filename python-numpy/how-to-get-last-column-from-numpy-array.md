# How to get last column from Numpy array

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
row = arr[:,-1]
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `[[1, 2], [3, 4]]` - sample matrix data (2-dimensional array)
- `np.array` - declare Numpy array
- `arr` - variable contains array
- `[:,-1]` - return last column of a given matrix

group: get_col

## Example: 
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
print(arr)

row = arr[:,-1]
print(row)
```
```
[[1 2]
 [3 4]]
[2 4]

```

