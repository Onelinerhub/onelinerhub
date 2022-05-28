# How to plot bestfit line

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7])
y = np.array([6, 6, 7, 8])
plt.plot(x, y, 'o')

a, b = np.polyfit(x, y, 1)

plt.plot(x, a*x + b)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `[1, 3, 5, 7]` - list of x coordinates of dots to plot best fit regression from
- `[6, 6, 7, 8]` - list of y coordinates of dots to plot best fit regression from
- `plt.plot(x, y, 'o')` - plot our dots
- `polyfit` - calculates least square polynomial fit 
- `a*x + b` - we plot 1-st degree polynomial using calculated `a` and `b` 
- `.show()` - render chart in a separate window

group: bestfit

## Example: 
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7])
y = np.array([6, 6, 7, 8])
plt.plot(x, y, 'o')

a, b = np.polyfit(x, y, 1)

plt.plot(x, a*x + b)

plt.show()
```

