# How to change chart font size

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', size=20)
plt.plot([2,1,3])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `font` - we want to change font params
- `size` - set font `size` value
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

group: font

## Example: 
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', size=20)
plt.plot([2,1,3])
plt.show()
```

