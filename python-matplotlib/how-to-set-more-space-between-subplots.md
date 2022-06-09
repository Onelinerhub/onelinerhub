# How to set more space between subplots

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot([1,3,2])
axes[1].plot([8,2,5])
plt.subplots_adjust(wspace=0.6, hspace=0.6)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `.plot(` - plot specified data
- `.subplots_adjust(` - set subplot positioning params
- `wspace` - horizontal subplots spacing
- `hspace` - vertical subplots spacing
- `.show()` - render chart in a separate window

group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot([1,3,2])
axes[1].plot([8,2,5])
plt.subplots_adjust(wspace=0.6, hspace=0.6)

plt.show()
```

