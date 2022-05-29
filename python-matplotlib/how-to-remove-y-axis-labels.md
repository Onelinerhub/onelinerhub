# How to remove y-axis labels

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.yticks([], [])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `ytick` - setup x-axis ticks params
- `[], []` - this will set empty list for ticks, thus remove them
- `.show()` - render chart in a separate window

group: ticks

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.yticks([], [])
plt.show()
```

