# How to make equal axes

### Using `set_aspect()` can help make sure axes are equal:

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3])
ax = plt.gca()
ax.set_aspect(1)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.gca()` - returns current axes object
- `set_aspect(1)` - make chart aspect ratio is 1:1
- `.show()` - render chart in a separate window

group: axis_range

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,3])
ax = plt.gca()
ax.set_aspect(1)
plt.show()
```

