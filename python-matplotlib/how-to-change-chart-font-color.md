# How to change chart font color

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('text', color='red')
mpl.rc('axes', labelcolor='orange')
mpl.rc('xtick', color='blue')
mpl.rc('ytick', color='green')

plt.plot([2,1,3])
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Example')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `'text', color` - title color
- `'axes', labelcolor` - axes labels color
- `'xtick', color` - x value labels color
- `'ytick', color` - y value labels color
- `.show()` - render chart in a separate window

group: font_color

## Example: 
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('text', color='red')
mpl.rc('axes', labelcolor='orange')
mpl.rc('xtick', color='blue')
mpl.rc('ytick', color='green')

plt.plot([2,1,3])
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Example')

plt.show()
```

