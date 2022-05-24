# How to change plot background color

```python
import matplotlib.pyplot as plt
plt.figure().patch.set_facecolor('cyan')
plt.axes().set_facecolor('black')
plt.plot([2,1,2,2])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `plt.figure()` - returns plot figure object
- `set_facecolor` - sets object background
- `plt.axes()` - returns chart object
- `cyan` - set this color as an outer background
- `black` - set this color as a chart background
- `.show()` - render chart in a separate window

group: background

## Example: 
```python
import matplotlib.pyplot as plt
plt.figure().patch.set_facecolor('cyan')
plt.axes().set_facecolor('black')
plt.plot([2,1,2,2])
plt.show()
```

