# How to check if arrays are equal

```python
import numpy as np

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[1, 2], [3, 4]])

is_equal = (a1==a2).all()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `a1` - first sample array
- `a2` - second sample array
- `is_equal` - will contain `True` if `a1` and `a2` are equal
- `(a1==a2).all()` - will return `True` if all elements of given arrays are equal

## Example: 
```python
import numpy as np

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[1, 2], [3, 4]])
a3 = np.array([[1, 2], [3, 5]])

print( (a1==a2).all() )
print( (a1==a3).all() )
```
```
True
False

```

