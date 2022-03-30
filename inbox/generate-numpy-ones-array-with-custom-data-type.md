# Generate Numpy ones array with custom datatype

```python
import numpy as np
a = np.ones((2, 3),dtype='int64')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.ones` - generates ones array
- `(2, 3)` - generated array dimensions (`2x3` in our case)
- `dtype='int64'` data type of generated array. See [here](https://www.w3resource.com/numpy/data-types.php) for a list of data types.

group: array_generate

## Example: 
```python
import numpy as np
a = np.ones((2, 3),dtype='int64')
print(a)
```
```
[[1. 1. 1.]
 [1. 1. 1.]]

```

