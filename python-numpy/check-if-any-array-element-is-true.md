# Check if any array element is True

```python
import numpy as np

a = np.array([False, True, False])

has_true = a.any()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.any()` - will return `True` if any array of a given element is `True`

group: check_true

## Example: 
```python
import numpy as np

a = np.array([False, True, False])

print( a.any() )
```
```
True

```

