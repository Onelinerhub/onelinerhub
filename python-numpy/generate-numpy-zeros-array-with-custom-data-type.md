# Generate Numpy zeros array with custom data type

```python
import numpy as np
a = np.zeros((2, 3), dtype='int64')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.zeros` - generates zeros array
- `(2, 3)` - generated array dimensions (`2x3` in our case)
- `dtype='int64'` - Numpy numeric data type to use

group: array_generate

## Example: 
```python
import numpy as np
a = np.zeros((2, 3), dtype='int64')
print(a)
```
```
[[0 0 0]
 [0 0 0]]

```

