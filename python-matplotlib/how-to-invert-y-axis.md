# How to invert Y axis

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.gca().invert_yaxis()
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.gca()` - returns current axes object
- `invert_yaxis()` - inverts `Y` axis
- `.show()` - render chart in a separate window

group: reverse

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,5,3,3,4,5,2,1])
plt.gca().invert_yaxis()
plt.show()
```

