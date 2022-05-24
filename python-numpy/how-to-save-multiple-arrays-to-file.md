# How to save multiple arrays to file

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([9,8,7])
np.savez('/tmp/numpies', a, b)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.savez` - save specified arrays to a file
- `/tmp/numpies` - path to file to save array to (file will have `npz` extension)

group: file

## Example: 
```python
import numpy as np

a = np.array([1,2,3])
b = np.array([9,8,7])
np.savez('/tmp/numpies', a, b)

import os
print(os.path.getsize("/tmp/numpies.npz"))
```
```
554

```

