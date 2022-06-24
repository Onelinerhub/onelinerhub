# How to use Numpy binary search

```python
import numpy as np

array = np.array([1,2,3,8])
idx = np.searchsorted(array, 5)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.searchsorted` - uses binary search to find position to insert specified value in order to keep array sorted
- `array` - array to search in
- `5` - value to search insertion position of

## Example: 
```python
import numpy as np

array = np.array([1,2,3,8])
idx = np.searchsorted(array, 5)

print(idx)
```
```
3

```

link_youtube: https://youtu.be/dJR8l3OsMPU
