# Generate empty Numpy array

```python
import numpy as np
arr = np.empty(5)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.empty` - generate empty Numpy array of the specified shape
- `(5)` - sample shape to generate (1-dimensional array of 5 elements in our case)
- `arr` - generated array

group: generate

## Example: 
```python
import numpy as np
a = np.empty(5)
print(a.shape)
```
```
(5,)

```

