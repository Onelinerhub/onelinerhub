# How to get first column from Numpy array COPY

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
row = arr[:,0]
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `[[1, 2], [3, 4]]` - sample matrix data (2-dimensional array)
- `np.array` - declare Numpy array
- `arr` - variable contains array
- `[:,0]` - return first column ('0' index is for first column)

group: get_col

## Example: 
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
print(arr)

row = arr[:,0]
print(row)
```
```
[[1 2]
 [3 4]]
[1 3]

```

