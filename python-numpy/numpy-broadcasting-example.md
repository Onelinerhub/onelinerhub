# Numpy broadcasting example

```python
import numpy as np

a = np.array([1, 2, 3])
b = 3

result = a * b
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `a * b` - during this operation `b` value will be broadcasted to all values of `a` array

## Example: 
```python
import numpy as np

a = np.array([1, 2, 3])
b = 3

print(a * b)
```
```
[3 6 9]

```

link_youtube: https://youtu.be/5twnpgA4mAY
