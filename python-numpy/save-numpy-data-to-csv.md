# Save Numpy data to CSV

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
np.savetxt('/tmp/numpy.csv', a)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.savetxt(` - save given Numpy array into `CSV` file

group: csv

## Example: 
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
np.savetxt('/tmp/numpy.csv', a)

with open('/tmp/numpy.csv', 'r') as f:
  print(f.read())
```
```
1.000000000000000000e+00
2.000000000000000000e+00
3.000000000000000000e+00
4.000000000000000000e+00
5.000000000000000000e+00


```

