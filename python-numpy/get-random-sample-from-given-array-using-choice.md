# Get random sample from given array using choice()

```python
import numpy as np
a = np.array([1,2,3,6,7,8])
sample = np.random.choice(a, 3)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1,2,3,6,7,8]` - array to get random sample from
- `.random.choice` - returns random array from given array of a given size
- `a, 3` - return array from `a` array of `3` elements long
- `sample` - will contain random sample from array

## Example: 
```python
import numpy as np
a = np.array([1,2,3,6,7,8])
sample = np.random.choice(a, 3)
print(sample)
```
```
[1 7 1]

```

