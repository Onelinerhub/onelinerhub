# Get array size

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
size = arr.size
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data
- `.size` - attribute contains number of elements in an array
- `size` - will contain given array size

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print('size:', arr.size)
```
```
size: 4

```

