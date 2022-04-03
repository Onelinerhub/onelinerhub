# How to sort Numpy array descending

```python
import numpy as np
a = np.array([3, 1, 4, 2, 5])

sorted = -np.sort(-a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `-np.sort(-a)` - will sort negative values of a given `a` array and then change values signs (magic to sort in descending order)
- `sorted` - will contain sorted array

group: sort

## Example: 
```python
import numpy as np
a = np.array([3, 1, 4, 2, 5])

sorted = -np.sort(-a)
print(sorted)
```
```
[5 4 3 2 1]

```

