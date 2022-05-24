# How to load Numpy array from text file

```python
import numpy as np

array = np.loadtxt('/tmp/numpy.txt')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.loadtxt` - load array from text file
- `/tmp/numpy.txt` - path to text file that was previously saved with [savetxt()](/python-numpy/how-to-save-numpy-array-to-text-file)
- `array` - will contain loaded array

group: text_file

## Example: 
```python
import numpy as np

array = np.loadtxt('/tmp/numpy.txt')
print(array)
```
```
[1. 2. 3. 4. 5.]

```

