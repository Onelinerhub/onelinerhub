# How to use LaTeX font

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "monospace"})
plt.title('Other Font')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `title` - set chart title
- `.rcParams.update` - update plot configuration
- `text.usetex` - enables [`LaTeX` usage](https://matplotlib.org/3.5.0/tutorials/text/usetex.html)
- `font.family` - specify font to use
- `.show()` - render chart in a separate window

group: font_name

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "monospace"})
plt.title('Other Font')
plt.show()
```

