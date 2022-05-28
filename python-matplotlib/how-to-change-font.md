# How to change font

```python
import matplotlib.pyplot as plt
plt.plot([2,1,3])
plt.title('Other Font', fontname='monospace')
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
plt.title('Other Font', fontname='monospace')
plt.show()
```

