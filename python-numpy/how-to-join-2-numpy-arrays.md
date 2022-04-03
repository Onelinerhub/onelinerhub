# How to join 2 Numpy arrays

```python
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

joined = np.concatenate((a, b))
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.concatenate` - joins a sequence of arrays
- `(a, b)` - arrays to join
- `joined` - resulting array of values from joined arrays

group: join

## Example: 
```python
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a, b)))
```
```
[1 2 3 4 5 6 7 8]

```

