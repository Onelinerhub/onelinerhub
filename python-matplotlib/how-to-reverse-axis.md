# How to invert X axis

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.gca().invert_xaxis()
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.gca()` - returns current axes object
- `invert_xaxis()` - inverts `X` axis
- `.show()` - render chart in a separate window

group: reverse

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.gca().invert_xaxis()
plt.show()
```

