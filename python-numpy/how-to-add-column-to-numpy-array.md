# How to add column to Numpy array

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
arr = np.append(arr, [[5], [6]], axis=1)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample 2-dimensional array to add new column to
- `np.append` - append values to specified array
- `arr` - array to append column to
- `[[5], [6]]` - new column values to append
- `axis=1` - append new values along vertical (`1`) axis

group: add_new

## Example: 
```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
a = np.append(a, [[5], [6]], axis=1)
print(a)
```
```
[[1 2 5]
 [3 4 6]]

```

