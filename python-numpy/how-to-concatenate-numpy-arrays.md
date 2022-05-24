# How to concatenate Numpy arrays

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([5, 6, 7])

joined = np.concatenate((a, b))
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `(a, b)` - arrays to concatenate (you can concatenate any number of arrays)
- `np.concatenate` - joins a sequence of arrays
- `joined` - resulting array of values from joined arrays

group: join

## Example: 
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([5, 6, 7])

joined = np.concatenate((a, b))
print(joined)
```
```
[1 2 3 5 6 7]

```

