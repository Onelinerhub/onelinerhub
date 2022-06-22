# How to build histogram for 2-dimensional array

```python
import numpy as np

x = np.array([5,6,6])
y = np.array([1,2,2])
hres = np.histogram2d(x, y, 3)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.histogram2d` - build 2-dimensional histogram
- `x, y` - first and second dimension
- `3` - number of bins to automatically create
- `hres` - will contain calculated histogram as a list of `[histogram, bin1, bin2]`

group: histogram

## Example: 
```python
import numpy as np

x = np.array([5,6,6])
y = np.array([1,2,2])
hres = np.histogram2d(x, y, 3)

print(hres)

```
```
(array([[1., 0., 0.],
       [0., 0., 0.],
       [0., 0., 2.]]), array([5.        , 5.33333333, 5.66666667, 6.        ]), array([1.        , 1.33333333, 1.66666667, 2.        ]))

```

link_youtube: https://youtu.be/oXHV0mTC3VM
