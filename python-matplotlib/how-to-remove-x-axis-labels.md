# How to remove x-axis labels

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xticks([], [])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `xtick` - setup x-axis ticks params
- `[], []` - this will set empty list for ticks, thus remove them
- `.show()` - render chart in a separate window

group: ticks

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xticks([], [])
plt.show()
```

