# How to sort Numpy array

```python
import numpy as np
a = np.array([3, 1, 4, 2, 5])

sorted = np.sort(a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.sort` - returns a sorted copy of an array
- `sorted` - will contain sorted array

group: sort

## Example: 
```python
import numpy as np
a = np.array([3, 1, 4, 2, 5])

sorted = np.sort(a)
print(sorted)
```
```
[1 2 3 4 5]

```

