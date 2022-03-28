# How to use zip for Numpy arrays

```python
import numpy as np
a1 = [1,2,3]
a2 = [5,6,7]
za = np.array([arr for arr in zip(a1, a2)])
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `a1` - first sample array

## Example: 
```python
import numpy as np
a1 = [1,2,3]
a2 = [5,6,7]
za = np.array([arr for arr in zip(a1, a2)])
print(za)
```
```
[]

```

