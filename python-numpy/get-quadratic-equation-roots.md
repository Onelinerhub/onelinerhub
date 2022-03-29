# Get quadratic equation roots

```python
import numpy as np
arr = np.array([1, 4, 4]) # x^2 + 4*x + 4
roots = np.roots(arr)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1, 4, 4]` - this array declares sample polynom `x^2 + 4*x + 4` to get roots for
- `.roots(` - return array with roots
- `roots` - will contain calculated roots

group: polynomial

## Example: 
```python
import numpy as np
arr = np.array([1, 4, 4])
roots = np.roots(arr)
print(roots)
```
```
[-2. -2.]

```

