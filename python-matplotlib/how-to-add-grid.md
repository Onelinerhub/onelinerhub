# How to add grid to chart

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4])
plt.plot([4,2,11,2,1,20,25])
plt.grid(True)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.grid(` - add and configure grid
- `.show()` - render chart in a separate window

group: grid

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4])
plt.plot([4,2,11,2,1,20,25])
plt.grid(True)
plt.show()
```

