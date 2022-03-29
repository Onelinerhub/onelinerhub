# How to generate empty Numpy matrix

```python
import numpy as np
matrix = np.empty([5, 4])
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.empty` - generate empty Numpy array of the specified shape
- `[5, 4]` - we will generate `5x4` empty matrix
- `matrix` - will contain generated Numpy matrix

group: generate

## Example: 
```python
import numpy as np
a = np.empty([5, 4])
print(a.shape)
```
```
(5, 4)

```

