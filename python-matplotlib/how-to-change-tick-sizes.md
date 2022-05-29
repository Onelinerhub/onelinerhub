# How to change tick sizes

### In order to change axis labels frequency, we can use `nbins` option of `locator_params` to set the amount of ticks we want:

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.tick_params(axis='both', length=15)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `tick_params` - set axis tick labels params
- `axis='both'` - we want to update configuration for all axes (use `x` or `y` to update certain axis)
- `length` - set length of the ticks
- `15` - length of our ticks would be 15 points
- `.show()` - render chart in a separate window

group: tick

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.tick_params(axis='both', length=15)
plt.show()
```

