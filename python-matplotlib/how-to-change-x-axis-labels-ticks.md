# How to change x axis labels (ticks)

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xticks([0,1,2], ['A', 'B', 'C'])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `xticks(` - set labels for x-axis values (ticks)
- `[0,1,2]` - list of ticks to set values for (index starts at `0`) 
- `['A', 'B', 'C']` - labels to use for ticks
- `.show()` - render chart in a separate window

group: ticks

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xticks([0,1,2], ['A', 'B', 'C'])
plt.show()
```

