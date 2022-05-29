# How to set font style to italic

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', style='italic')
plt.plot([2,1,3])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `font` - change font settings
- `style` - set font style (`italic` in our case)
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

group: font_italic

## Example: 
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font', style='italic')
plt.plot([2,1,3])

plt.show()
```

