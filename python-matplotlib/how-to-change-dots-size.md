# How to change dot size

```python
import matplotlib.pyplot as plt

plt.plot([1, 3, 5, 7], [6, 6, 7, 8], 'o', ms=15)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `[1, 3, 5, 7]` - x coordinates
- `[6, 6, 7, 8]` - y coordinates
- `'o'` - don't draw a line, only circle dots
- `ms=` - sets the size of the dot
- `.show()` - render chart in a separate window

group: dots

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([1, 3, 5, 7], [6, 6, 7, 8], 'o', ms=15)

plt.show()
```

