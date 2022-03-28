# How to convert Python list to Numpy array

```python
import numpy as np

lst = [1, 2, 3]
a = np.array(lst)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `[1, 2, 3]` - sample Python list
- `np.array` - create Numpy array from given list

group: list

## Example: 
```python
import numpy as np

lst = [1, 2, 3]
a = np.array(lst)

print(a)
print(type(a))
```
```
[1 2 3]
<class 'numpy.ndarray'>

```

