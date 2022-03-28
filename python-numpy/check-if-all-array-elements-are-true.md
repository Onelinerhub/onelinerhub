# Check if all array elements are True

```python
import numpy as np

a = np.array([True, True, True])

all_true = a.all()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.all()` - will return `True` if all array of a given element are `True`

group: check_true

## Example: 
```python
import numpy as np

a = np.array([True, True, True])

print( a.all() )
```
```
True

```

