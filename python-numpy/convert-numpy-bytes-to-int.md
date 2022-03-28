# Convert Numpy bytes to int

```python
import numpy as np
a = np.frombuffer(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00', dtype=np.uint32)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.frombuffer(` - converts given bytes to array with the specified type
- `dtype=np.uint32` - specify one of [Numpy type](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types) to use to convert from bytes

group: bytes

## Example: 
```python
import numpy as np
a = np.frombuffer(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00', dtype=np.uint32)
print(a)
```
```
[1 2 3]

```

