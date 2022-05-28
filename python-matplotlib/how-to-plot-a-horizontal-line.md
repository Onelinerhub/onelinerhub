# How to plot a horizontal line

```python
import matplotlib.pyplot as plt
plt.axline([0,1], [1,1])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `axline` - draws a line based on 2 points
- `[0,1], [1,1]` - 2 points of horizontal line going through `1` on `y` axis
- `.show()` - render chart in a separate window

group: line_std

## Example: 
```python
import matplotlib.pyplot as plt
plt.axline([0,1], [1,1])
plt.show()
```

