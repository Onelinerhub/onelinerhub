# How to change y axis labels (ticks)

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.yticks([2,1,3], ['20a', '10b', '30c'])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `yticks(` - set labels for y-axis values (ticks)
- `[2,1,3]` - list of ticks to set labels for (= list of y-axis values)
- `['20a', '10b', '30c']` - labels to use for ticks
- `.show()` - render chart in a separate window

group: ticks

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.yticks([2,1,3], ['20a', '10b', '30c'])
plt.show()
```

