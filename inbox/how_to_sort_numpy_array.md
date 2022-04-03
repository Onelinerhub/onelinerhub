# How to sort Numpy array

```python
import numpy as np
a = np.array([3, 1, 4, 2, 5])

np.sort(a)      # sort in ascending order
-np.sort(-a)    # sort in descending order
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.sort` - returns a sorted copy of an array

## Example
```python
import numpy as np
a = np.array([3, 1, 4, 2, 5])

print(np.sort(a))
print(-np.sort(-a))
```
```
[1 2 3 4 5]
[5 4 3 2 1]
```
