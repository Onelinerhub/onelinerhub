# How to draw a circle

```python
import matplotlib.pyplot as plt

figure, axes = plt.subplots()

axes.set_aspect(1)
axes.add_artist(plt.Circle((0.5, 0.5), .25))

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `set_aspect(1)` - make chart aspect ratio is 1:1
- `.Circle(` - plots a circle
- `0.5, 0.5` - circle center point coordinates
- `.25` - circle radius
- `.show()` - render chart in a separate window

group: circle

## Example: 
```python
import matplotlib.pyplot as plt

figure, axes = plt.subplots()

axes.set_aspect(1)
axes.add_artist(plt.Circle((0.5, 0.5), .25))

plt.show()
```

