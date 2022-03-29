# Get correlation of two Numpy arrays

```python
import numpy as np

a1 = np.array([1,1,2,1,2])
a2 = np.array([2,2,4,2,4])

cor = np.corrcoef(a1, a2)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `a1` - first sample array
- `a2` - second sample array
- `.corrcoef(` - return [Pearson product-moment correlation](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html) coefficients of specified arrays
- `cor` - will contain generated coefficients matrix

## Example: 
```python
import numpy as np

a1 = np.array([1,1,2,1,2])
a2 = np.array([2,2,6,2,5])

cor = np.corrcoef(a1, a2)
print(cor)
```
```
[[1.        0.9834151]
 [0.9834151 1.       ]]

```

