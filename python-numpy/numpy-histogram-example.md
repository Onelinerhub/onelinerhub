# Numpy histogram example

```python
import numpy as np
array = np.array([5,6,6])
histres = np.histogram(array, 2)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.histogram` - calculates histogram for specified array and bins
- `2` - this means we want to automatically create 3 bins for our histogram
- `histres` - will contain calculated histogram

group: histogram

## Example: 
```python
import numpy as np
array = np.array([5,6,6])
hist = np.histogram(array, 2)
print(hist)
```
```
(array([1, 2]), array([5. , 5.5, 6. ]))

```

link_youtube: https://youtu.be/6GG_k5C76Xo
