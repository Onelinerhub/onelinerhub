# How to change axis label color

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('axes', labelcolor='red')

plt.plot([2,1,3])
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `'axes', labelcolor` - axes labels color
- `.show()` - render chart in a separate window

group: font

## Example: 
```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('axes', labelcolor='red')

plt.plot([2,1,3])
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

