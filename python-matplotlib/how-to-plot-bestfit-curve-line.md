# How to plot bestfit curve line

### In order to make curved line, we have to increase degree of our polynomial (3rd argument to `polyfit()`):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7])
y = np.array([6, 6, 7, 8])
plt.plot(x, y, 'o')

a, b, c = np.polyfit(x, y, 2)

plt.plot(x, a * x*x + b*x + c)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `[1, 3, 5, 7]` - list of x coordinates of dots to plot best fit regression from
- `[6, 6, 7, 8]` - list of y coordinates of dots to plot best fit regression from
- `polyfit` - calculates least square polynomial fit
- `a * x*x + b*x + c` - we plot 2-degree polynomial to get curved best fit regression line
- `.show()` - render chart in a separate window

group: bestfit

## Example: 
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 5, 7])
y = np.array([6, 6, 7, 8])
plt.plot(x, y, 'o')

a, b, c = np.polyfit(x, y, 2)

plt.plot(x, a * x*x + b*x + c)

plt.show()
```

