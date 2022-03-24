# Simple example of Numpy usage

```python
import numpy as np

a = np.array([1, 3, 5, 9])

mean_a = a.mean(axis=0)
print(mean_a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1, 3, 5, 9]` - sample array to create
- `.mean` - find mean for given array
- `print(mean_a)` - output found mean value

group: quickstart

## Example: 
```python
import numpy as np

a = np.array([1, 3, 5, 9])

mean_a = a.mean()
print(mean_a)
```

