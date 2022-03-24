# Create 3-dimensional array

```python
import numpy as np
a = np.array([
  [ [1, 2, 3], [3, 4, 5], [2, 4, 6] ],
  [ [5, 6, 7], [7, 8, 9], [6, 7, 9] ],
  [ [3, 2, 1], [2, 4, 6], [1, 2, 3] ],
])
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array

group: create_array

## Example: 
```python
import numpy as np
a = np.array([
  [ [1, 2, 3], [3, 4, 5], [2, 4, 6] ],
  [ [5, 6, 7], [7, 8, 9], [6, 7, 9] ],
  [ [3, 2, 1], [2, 4, 6], [1, 2, 3] ],
])
print(a)
```
```
[[[1 2 3]
  [3 4 5]
  [2 4 6]]

 [[5 6 7]
  [7 8 9]
  [6 7 9]]

 [[3 2 1]
  [2 4 6]
  [1 2 3]]]

```

