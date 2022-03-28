# Convert Numpy bytes to array

```python
import numpy as np

bts = b'\x01\x02\x03'

a = np.array(np.frombuffer(bts, dtype=np.uint8));
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `b'\x01\x02\x03'` - sample byte string
- `.frombuffer(` - converts given bytes to array with the specified type
- `dtype=np.uint8` - specify one of [Numpy type](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types) to use to convert from bytes
- `np.array` - create Numpy array from given list

group: bytes

## Example: 
```python
import numpy as np

a = np.array([1, 2, 3], dtype=np.uint8)
bts = a.tobytes()
print(bts)

a = np.array(np.frombuffer(bts, dtype=np.uint8));
print(a)
```
```
b'\x01\x02\x03'
[1 2 3]

```

