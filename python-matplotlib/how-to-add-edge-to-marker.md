# How to add outline (edge) to marker

```python
import matplotlib.pyplot as plt

plt.scatter(2,3,s=900,color='cyan',edgecolors='black')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.scatter(` - plots a single point
- `2,3` - `x` and `y` coordinates
- `edgecolors` - set border color of a point
- `.show()` - render chart in a separate window

group: marker

## Example: 
```python
import matplotlib.pyplot as plt

plt.scatter(2,3,s=900,color='cyan',edgecolors='black')

plt.show()
```

