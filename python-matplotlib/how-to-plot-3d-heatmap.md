# How to plot 3D heatmap

### Instead of using [`imshow()`](/python-matplotlib/how-to-plot-heatmap) we could use `scatter()` method to plot 3D heatmap:

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
  
x = np.random.randint(low=100, high=500, size=(50,))
y = np.random.randint(low=300, high=500, size=(50,))
z = np.random.randint(low=200, high=500, size=(50,))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

color_map = cm.ScalarMappable(cmap=cm.Reds_r)
clr = [x + y + z]
color_map.set_array(clr)

img = ax.scatter(x, y, z, s=200, color='red')
plt.colorbar(color_map)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.random.randint` - generates random array based on specified paras (50 elements in our case)
- `.add_subplot` - create sub chart
- `cm.ScalarMappable` - create color map to use for points
- `.set_array(` - apply our values (sum of x/y/z coordinates for each point) to color map
- `.scatter(` - plots a point chart
- `.colorbar(` - draw color bar based on our data
- `.show()` - render chart in a separate window

group: heatmap

## Example: 
```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
  
x = np.random.randint(low=100, high=500, size=(50,))
y = np.random.randint(low=300, high=500, size=(50,))
z = np.random.randint(low=200, high=500, size=(50,))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

color_map = cm.ScalarMappable(cmap=cm.Reds_r)
clr = [x + y + z]
color_map.set_array(clr)

img = ax.scatter(x, y, z, s=200, color='red')
plt.colorbar(color_map)

plt.show()
```

