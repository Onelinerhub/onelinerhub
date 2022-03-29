# Get cubic equation roots

```python
import numpy as np
arr = np.array([1, 24, -32, 1]) # x^3 + 24*x^2 - 32*x + 1
roots = np.roots(arr)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1, 24, -32, 1]` - this array declares sample polynom `x^3 + 24*x^2 - 32*x + 1` to get roots for
- `.roots(` - return array with roots
- `roots` - will contain calculated roots

group: polynomial

## Example: 
```python
import numpy as np
arr = np.array([1, 24, -32, 1])
roots = np.roots(arr)
print(roots)
```
```
[-25.26799065   1.23597066   0.03201999]

```

