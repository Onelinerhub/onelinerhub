# Append new values to array

```python
import numpy as np
arr = np.array([[1, 2]])
arr = np.append(arr, [[3, 4]], axis=0)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2]]` - sample 2-dimensional array
- `np.append` - append values to specified array
- `arr` - array to append new values to
- `[[3, 4]]` - new values array to append to `arr` (should have the same dimension count)
- `axis=0` - axis to add new values along

group: add_new

## Example: 
```python
import numpy as np
a = np.array([[1, 2]])
a = np.append(a, [[3, 4]], axis=0)
print(a)
```
```
[[1 2]
 [3 4]]

```

