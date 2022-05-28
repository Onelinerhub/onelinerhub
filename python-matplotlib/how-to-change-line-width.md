# How to change line width

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], linewidth=5)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `[1,2,10,6,15,3,4]` - values to use for first line
- `linewidth` - set width of line
- `.show()` - render chart in a separate window

group: line

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], linewidth=5)
plt.show()
```

