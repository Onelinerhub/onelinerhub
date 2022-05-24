# How to save array to file

```python
import numpy as np

array = np.array([1,2,3])
np.save('/tmp/numpy', array)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.save` - save array to file
- `/tmp/numpy` - path to file to save array to (file will have `npy` extension)
- `array` - array to save to file

group: file

## Example: 
```python
import numpy as np

array = np.array([1,2,3])
np.save('/tmp/numpy', array)

import os
print(os.path.getsize("/tmp/numpy.npy"))
```
```
152

```

