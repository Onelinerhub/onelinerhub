# How to change marker size

```python
import matplotlib.pyplot as plt

plt.scatter(2,3,s=300)
plt.scatter(4,7,s=900)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.scatter(` - plots a single point
- `2,3` - `x` and `y` coordinates of first point
- `s=300` - set point size to 300
- `4,7` - `x` and `y` coordinates of second point
- `s=900` - set point size to 900
- `.show()` - render chart in a separate window

group: marker

## Example: 
```python
import matplotlib.pyplot as plt

plt.scatter(2,3,s=300)
plt.scatter(4,7,s=900)

plt.show()
```

