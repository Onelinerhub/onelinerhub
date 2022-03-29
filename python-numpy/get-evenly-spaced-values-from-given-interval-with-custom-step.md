# Get evenly spaced values from given interval with custom step

```python
import numpy as np 
a = np.arange(10, 20, 3)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.arange(` - generates evenly spaced array based on specified range
- `10, 20` - range to generate array from (from `10` inclusive to `20` not inclusive in our case)
- `, 3` - step size for generated values

group: even

## Example: 
```python
import numpy as np 
a = np.arange(10, 20, 3)


print(a)
```
```
[10 13 16 19]

```

