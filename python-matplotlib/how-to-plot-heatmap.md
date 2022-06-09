# How to plot heatmap

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
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
im = ax.imshow([[0.8, 2.4, 2.5], [1.3, 1.2, 0.0], [0.1, 2.0, 0.0]])

plt.show()
```

