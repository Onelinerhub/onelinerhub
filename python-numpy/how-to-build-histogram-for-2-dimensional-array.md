# How to build histogram for 2-dimensional array

```python
import numpy as np

x = np.array([5,6,6])
y = np.array([1,1,2])
H, xe, ye = np.histogram2d(x, y, [3,3])
```


group: histogram

## Example: 
```python
import numpy as np

x = np.array([5,6,6])
y = np.array([1,2,2])
hres, xb, yb = np.histogram2d(x, y, 2)

print(hres)
```
```
[[1. 0. 0.]
 [0. 0. 0.]
 [1. 0. 1.]]

```

