# How to get unique values from Numpy array

```python
import numpy as np
a = np.array([1,1,2,1,2])
uniq = np.unique(a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1,1,2,1,2]` - sample array
- `.unique(` - returns unique values only from specified array
- `uniq` - will contain array with unique values only

group: uniq

## Example: 
```python
import numpy as np
a = np.array([1,1,2,1,2])
uniq = np.unique(a)
print(uniq)
print(type(uniq))
```
```
[1 2]
<class 'numpy.ndarray'>

```

