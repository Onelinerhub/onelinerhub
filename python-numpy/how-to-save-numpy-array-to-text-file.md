# How to save Numpy array to text file	

```python
import numpy as np

array = np.array([1,2,3,4,5])
np.savetxt('/tmp/numpy.txt', array)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.savetxt` - saves specified array to text file
- `/tmp/numpy.txt` - path to text file to save array to
- `array` - array to save to text file

group: text_file

## Example: 
```python
import numpy as np

array = np.array([1,2,3,4,5])
np.savetxt('/tmp/numpy.txt', array)

import os
print(os.path.getsize('/tmp/numpy.txt'))
```
```
125

```

