# How to save numpy data to CSV

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
np.savetxt('my_array.csv', a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.savetxt` - save array as text file, specifying '.csv' as filename 
