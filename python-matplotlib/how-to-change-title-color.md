# How to change title color

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('text', color='red')

plt.plot([2,1,3])
plt.title('Example')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `'text', color` - set color of title
- `.show()` - render chart in a separate window

group: font

## Example: 
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('text', color='red')

plt.plot([2,1,3])
plt.title('Example')

plt.show()
```

