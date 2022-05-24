# How to save Numpy matrix to text file

```python
import numpy as np

matrix = np.array([[1,2], [3,4], [5,6]])
np.savetxt('/tmp/db.csv', matrix)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array (or matrix)
- `.savetxt` - saves specified matrix to text file
- `/tmp/matrix.txt` - path to text file to save matrix to
- `matrix` - matrix to save to text file

group: text_file

## Example: 
```python
import numpy as np

matrix = np.array([[1,2], [3,4], [5,6]])
np.savetxt('/tmp/matrix.txt', matrix)

import os
print(os.path.getsize('/tmp/matrix.txt'))
```
```
150

```

