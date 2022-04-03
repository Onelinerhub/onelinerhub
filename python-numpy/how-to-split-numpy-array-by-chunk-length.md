# How to split Numpy array by chunk length

```python
import math
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
chunk_size = 2
split = np.array_split(a, math.ceil(a.size/chunk_size))
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.array_split` -  split array into specified number of sub-arrays; returns a list of sub-arrays
- `chunk_size` - number of elements in each chunk (chunk size) after split
- `math.ceil(a.size/chunk_size)` - calculate number of chunks to split by based on chunk size and given array size

group: split

## Example: 
```python
import math
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
chunk_size = 2
split = np.array_split(a, math.ceil(a.size/chunk_size))
print(split)
```
```
[array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]

```

