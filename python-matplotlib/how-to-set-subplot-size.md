# How to set subplot size

### In order to change subplots sizes we use `figsize()` method:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(4,2))

axes[0].plot([1,3,2])
axes[1].plot([8,2,5])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `figsize` - set figure size in inches (also [set dpi](/python-matplotlib/change-figure-size) to specify inch size in pixels)
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(4,2))

axes[0].plot([1,3,2])
axes[1].plot([8,2,5])

plt.show()
```

