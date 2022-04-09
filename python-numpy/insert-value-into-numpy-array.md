# Insert value into Numpy array

```python
import numpy as np
a = np.array([5, 6, 6])

np.insert(a, 3, 4)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.insert` - insert specified value at specified position
- `3` - position to insert new value at
- `4` - value to insert

group: insert_array

## Example: 
```python
import numpy as np
a = np.array([5, 6, 6])

print(np.insert(a, 3, 4))
```
```
[5 6 6 4]

```

