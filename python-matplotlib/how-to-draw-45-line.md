# How to draw 45° line

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot line from specified data
- `[1,2,10,6,15,3,4]` - values to use for plotted line
- `.show()` - render chart in a separate window

group: line_std

## Example: 
```python
import matplotlib.pyplot as plt
ax.axline([0, 0], [1, 1])
plt.show()
```

