# Insert values into Numpy array at multiple positions

```python
import numpy as np
a = np.array([5, 6, 6, 8, 9])

np.insert(a, [2, 4], 7)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.insert` - insert specified value at specified position
- `[2, 4]` - list of positions to insert given value at
- `7` - value to insert

group: insert_array

## Example: 
```python
import numpy as np
a = np.array([5, 6, 6, 8, 9])

print(np.insert(a, [2, 4], 7))
```
```
[5 6 7 6 8 7 9]

```

