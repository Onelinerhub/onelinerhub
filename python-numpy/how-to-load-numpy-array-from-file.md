# How to load Numpy array from file

### Before loading array data from file, you should [save Numpy array to file](/python-numpy/save-array-to-file).

```python
import numpy as np

array = np.load('/tmp/numpy.npy')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `array` - will contain loaded array from file
- `.load` - loads Numpy array from specified file
- `/tmp/numpy.npy` - path to Numpy array file that was [previously saved](/python-numpy/save-array-to-file)

group: file

## Example: 
```python
import numpy as np

array = np.load('/tmp/numpy.npy')
print(array)
```
```
[1 2 3]

```

