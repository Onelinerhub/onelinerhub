# How to use LaTeX font

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Georgia"]})
plt.title('Other Font')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `title` - set chart title
- `fontname` - set font face from the [list of supported fonts](/python-matplotlib/how-to-list-supported-fonts)
- `.show()` - render chart in a separate window

group: font_name

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Georgia"]})
plt.title('Other Font')
plt.show()
```

