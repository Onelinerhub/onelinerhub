# How to load multiple arrays from npz file

### This will work if multiple arrays were saved to [`npz` file using `savez`](/python-numpy/how-to-save-multiple-arrays-to-file) method.

```python
import numpy as np

z = np.load('/tmp/numpies.npz')

print(z.files)
print(z['arr_0'])
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.load` - loads Numpy array from specified file
- `/tmp/numpies.npz` - path to file to load from (`npz` means we're loading multiple arrays, that were [previously saved](/python-numpy/how-to-save-multiple-arrays-to-file))
- `z['arr_0']` - access first loaded array
- `z.files` - access all loaded arrays

group: file

## Example: 
```python
import numpy as np

z = np.load('/tmp/numpies.npz')

print(z.files)
print(z['arr_0'])
print(z['arr_1'])
```
```
['arr_0', 'arr_1']
[1 2 3]
[9 8 7]

```

