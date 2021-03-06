# How to change dot type

```python
import matplotlib.pyplot as plt

plt.plot([1, 3, 5, 7], [6, 6, 7, 8], 'p', ms=15)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `[1, 3, 5, 7]` - x coordinates
- `[6, 6, 7, 8]` - y coordinates
- `'p'` - set dot type to `pentagon` from the list of [available types](https://matplotlib.org/stable/api/markers_api.html)
- `ms=` - sets the size of the dot
- `.show()` - render chart in a separate window

group: dots

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([1, 3, 5, 7], [6, 6, 7, 8], 'p', ms=15)

plt.show()
```

