# Convert Numpy array to bytes

```python
import numpy as np
a = np.array(['a', 'b', 'c'])
bts = a.tobytes()

```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `['a', 'b', 'c']` - sample array
- `.tobytes()` - converts given Numpy array to raw bytes

group: bytes

## Example: 
```python
import numpy as np
a = np.array(['a', 'b', 'c'])
print(a.tobytes())

```
```
b'a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'

```

