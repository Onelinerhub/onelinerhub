# Find Numpy array index by value

```python
import numpy as np
a = np.array([1,1,2,1,2])
indexes = np.where(a == 2)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[1,1,2,1,2]` - sample array
- `where(` - returns indexes of found elements from array based on condition
- `a == 2` - sample condition (search for elements with value `2`)

## Example: 
```python
import numpy as np
a = np.array([1,1,2,1,2])
indexes = np.where(a == 2)
print(indexes[0])
```
```
[2 4]

```

