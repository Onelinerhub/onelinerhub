# How to count unique values

```python
import numpy as np
a = np.array([1,1,2,1,2])
uniq = np.unique(a).size
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1,1,2,1,2]` - sample array
- `.unique(` - returns unique values only from specified array
- `.size` - attribute contains number of elements in an array
- `uniq` - will contain number of unique elements

group: uniq

## Example: 
```python
import numpy as np
a = np.array([1,1,2,1,2])
uniq = np.unique(a).size
print(uniq)
```
```
2

```

