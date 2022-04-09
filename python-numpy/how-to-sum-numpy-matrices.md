# How to sum Numpy matrices

```python
import numpy as np
a = np.matrix([[1, 1], [1, 1]])
b = np.matrix([[1, 1], [1, 1]])
sum_ar = np.add(a, b)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.matrix` - creates matrix from given data
- `np.add` - sums given matrices element-wise
- `sum_ar` - will contain resulting matrix

## Example: 
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

