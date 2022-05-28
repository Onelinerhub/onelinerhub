# How to plot a vertical line

```python
import matplotlib.pyplot as plt
plt.axline([1,0], [1,1])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `axline` - draws a line based on 2 points
- `[1,0], [1,1]` - 2 points of vertical line going through `1` on `x` axis
- `.show()` - render chart in a separate window

group: line_std

## Example: 
```python
import matplotlib.pyplot as plt
plt.axline([1,0], [1,1])
plt.show()
```

