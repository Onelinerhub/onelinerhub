# Generate random array of int values

```python
import numpy as np
arr = np.random.randint(10, 20, [3, 2])
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.random.randint(` - returns array of random int values in specified range of specified size
- `10, 20` - range to generate random int values from
- `[3, 2]` - array size to generate (`3x2` in our case)
- `arr` - generated array

group: random

## Example: 
```python
import numpy as np
arr = np.random.randint(10, 20, [3, 2])
print(arr)
```
```
[[16 18]
 [11 15]
 [17 11]]

```

