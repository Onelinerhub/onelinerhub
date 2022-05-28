# How to make bar chart with multiple columns using Numpy

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
plt.bar(x+0.2, [10, 11, 12], width=0.25)
plt.bar(x+0.5, [90, 85, 88], width=0.25)
plt.bar(x+0.8, [51, 50, 49], width=0.25)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array([1,2,3])` - define x-axis values as [Numpy array](/python-numpy/create-1-dimensional-array)
- `x+0.2, [10, 11, 12], width=0.25` - plot first column of each bar with `25%` width `[10,11,12]` values and `20%` offset from left
- `(x+0.5, [90, 85, 88], width=0.25)` - plot second column of each bar with `25%` width `[90, 85, 88]` values and `50%` offset from left
- `(x+0.8, [51, 50, 49], width=0.25)` - plot third column of each bar with `25%` width `[51, 50, 49]` values and `80%` offset from left
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
plt.bar(x+0.2, [10, 11, 12], width=0.25)
plt.bar(x+0.5, [90, 85, 88], width=0.25)
plt.bar(x+0.8, [51, 50, 49], width=0.25)
plt.show()
```

