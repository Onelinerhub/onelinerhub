# How to load Numpy matrix from text file

```python
import numpy as np

matrix = np.loadtxt('/tmp/matrix.txt')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.loadtxt` - load array from text file
- `/tmp/matrix.txt` - path to text file that was previously saved with [savetxt()](/python-numpy/how-to-save-numpy-matrix-to-text-file)
- `matrix` - will contain loaded matrix

group: text_file

## Example: 
```python
import numpy as np

matrix = np.loadtxt('/tmp/matrix.txt')
print(matrix)
```
```
[[1. 2.]
 [3. 4.]
 [5. 6.]]

```

