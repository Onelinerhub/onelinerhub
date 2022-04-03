# How to reverse Numpy array

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])

flipped = np.flip(a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.flip` - reverse specified array
- `flipped` - will contain reversed `a` array

## Example: 
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])

print(np.flip(a))
```
```
[5 4 3 2 1]

```

