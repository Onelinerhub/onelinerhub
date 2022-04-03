# How to split Numpy arrays

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

split = np.split(a, 2)
a1 = split[0]
a2 = split[1]
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.split` -  split array into specified number of equal sub-arrays; returns a list of sub-arrays
- `split(a, 2)` - splits `a` array into `2` equal sub-arrays
- `a1 = split[0]` - subset first sub-array and assign to new variable
- `a2 = split[1]` - subset second sub-array and assign to new variable

group: split

## Example: 
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

split = np.split(a, 2)
a1 = split[0]
a2 = split[1]

print(a1)
print(a2)
```
```
[1 2 3 4]
[5 6 7 8]

```

