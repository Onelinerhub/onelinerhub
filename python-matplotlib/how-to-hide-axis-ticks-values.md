# How to hide axis (ticks) values

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.gca()` - returns current axes object
- `set_ticks([])` - sets empty ticks list to hide labels
- `.show()` - render chart in a separate window

group: tick

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
plt.show()
```

