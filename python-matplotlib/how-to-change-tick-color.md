# How to change tick color

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('xtick', color='blue')
mpl.rc('ytick', color='green')

plt.plot([2,1,3])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `'xtick', color` - x value labels color
- `'ytick', color` - y value labels color
- `.show()` - render chart in a separate window

group: font

## Example: 
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('xtick', color='blue')
mpl.rc('ytick', color='green')

plt.plot([2,1,3])

plt.show()
```

