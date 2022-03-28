# Convert Numpy array to string

```python
import numpy as np

a = np.array([1, 2, 3, 4])
str = np.array2string(a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4]]` - sample matrix data (2-dimensional array)
- `.array2string(` - converts given Numpy array to string
- `str` - will contain resulting string

group: string

## Example: 
```python
import numpy as np

a = np.array([1, 2, 3, 4])
str = np.array2string(a)
print(type(str))
print(str)
```
```
<class 'str'>
[1 2 3 4]

```

