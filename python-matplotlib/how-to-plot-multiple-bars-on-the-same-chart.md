# How to plot multiple bars on the same chart

### In order to plot multiple lines, you simply call `plot()` method multiple times:

```python
import matplotlib.pyplot as plt

plt.bar(['a', 'b', 'c'], [1,4,2])
plt.bar(['a', 'b', 'c'], [2,5,1])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([1,4,2])
plt.plot([2,5,1])

plt.show()
```

