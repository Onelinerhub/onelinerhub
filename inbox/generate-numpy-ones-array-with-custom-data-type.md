# Generate Numpy ones array with custom datatype

```python
import numpy as np
a = np.ones((2, 3),dtype='float64')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.ones` - generates ones array
- `(2, 3)` - generated array dimensions (`2x3` in our case)
- `dtype='float64'` data type of generated array. 

group: array_generate

## Example: 
```python
import numpy as np
a = np.ones((2, 3),dtype='float64')
print(a)
```
```
[[1. 1. 1.]
 [1. 1. 1.]]

```

