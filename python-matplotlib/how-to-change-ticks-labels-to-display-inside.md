# How to change ticks to display inside the axes

### In order to change axis labels frequency, we can use `nbins` option of `locator_params` to set the amount of ticks we want:

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.tick_params(axis='x', direction='in')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `locator_params` - configure locator object
- `nbins` - sets the amount of tick labels to generate
- `.show()` - render chart in a separate window

group: tick

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.tick_params(axis='x', direction='in', length=10)
plt.show()
```

