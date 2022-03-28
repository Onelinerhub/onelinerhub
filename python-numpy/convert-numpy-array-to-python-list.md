# Convert Numpy array to Python list

```python
import numpy as np

a = np.array([1, 2, 3])
lst = a.tolist()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.tolist()` - converts Numpy array to list

group: list

## Example: 
```python
import numpy as np

a = np.array([1, 2, 3])
l = a.tolist()

print(l)
print(type(l))
```
```
[1, 2, 3]
<class 'list'>

```

