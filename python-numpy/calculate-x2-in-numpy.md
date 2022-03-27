# Calculate x^2 in Numpy

```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
arr = np.square(arr)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample array data
- `np.square` - calculates squares for each value in a given array
- `arr` - array to calculate squares for values of

## Example: 
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
arr = np.square(arr)
print(arr)
```
```
[[ 1  4]
 [ 9 16]]

```

