# Generate Numpy zeros array

```python
import numpy as np
a = np.zeros((2, 3))
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.zeros` - generates ones array
- `(2, 3)` - generated array dimensions (`2x3` in our case)

group: array_generate

## Example: 
```python
import numpy as np
a = np.zeros((2, 3))
print(a)
```
```
[[0. 0. 0.]
 [0. 0. 0.]]

```

## Example: with datatype specified
```python
import numpy as np
a = np.zeros((2,3),dtype='int64')
print(a)
```


