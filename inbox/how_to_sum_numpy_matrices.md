# How to sum Numpy matrices

```python
import numpy as np
a = np.matrix([[1, 1], [1, 1]])
b = np.matrix([[1, 1], [1, 1]])
np.add(a, b)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.matrix` - create Numpy matrix
- `np.add` - add arguments element-wise

## Example

```python
import numpy as np
a = np.matrix([[1, 1], [1, 1]])
b = np.matrix([[1, 1], [1, 1]])
print(np.add(a, b))
```
```
[[2 2]
 [2 2]]
```
