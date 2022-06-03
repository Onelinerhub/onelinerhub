# How to set Y axis range

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.ylim(-2, 5)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.ylim` - set min and max values for `Y` axis
- `.show()` - render chart in a separate window

group: axis_range

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.ylim(-2, 5)
plt.show()
```

