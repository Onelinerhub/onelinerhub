# How to plot 3D heatmap

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
im = ax.imshow([[0.8, 2.4, 2.5], [1.3, 1.2, 0.0], [0.1, 2.0, 0.0]])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `.imshow(` - displays data as an image (used for heatmaps from 2d arrays)
- `.show()` - render chart in a separate window

group: heatmap

## Example: 
```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
  
# creating a dummy dataset
x = np.random.randint(low=100, high=500, size=(1000,))
y = np.random.randint(low=300, high=500, size=(1000,))
z = np.random.randint(low=200, high=500, size=(1000,))
colo = [x + y + z]
  
# creating figures
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
  
# setting color bar
color_map = cm.ScalarMappable(cmap=cm.Greens_r)
color_map.set_array(colo)
  
# creating the heatmap
img = ax.scatter(x, y, z, marker='s',
                 s=200, color='green')
plt.colorbar(color_map)
  
# adding title and labels
ax.set_title("3D Heatmap")
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
  
# displaying plot
plt.show()
```

