# How to change grid color

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4,2,5,1,7,3,4])
plt.grid(color='green')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.grid(` - add and configure grid
- `color` - set color to use for grid lines
- `.show()` - render chart in a separate window

group: grid

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4,2,5,1,7,3,4])
plt.grid(color='green')
plt.show()
```

