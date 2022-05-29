# How to change ticks labels frequency

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.tick_params(axis='x', labelrotation=90)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `tick_params` - set axis tick labels params
- `axis='x'` - we want to update configuration for `x` axis only
- `labelrotation` - sets rotation for tick labels (degrees)
- `.show()` - render chart in a separate window

group: ticks

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.tick_params(axis='x', labelrotation=90)
plt(nbins=4)
plt.show()
```

