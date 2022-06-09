# Errorbar usage example

```python
import matplotlib.pyplot as plt

x = [2, 6, 15]
y = [20, 9, 15]

x_error = [2, 5.1, 1]

plt.bar(x,y)
plt.errorbar(x, y, xerr = x_error,ecolor = 'maroon',color='red')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `.errorbar(` - plots errorbars
- `x, y` - coordinates to plot errorbars at
- `x_error` - error bars sizes list
- `.show()` - render chart in a separate window

## Example: 
```python
import matplotlib.pyplot as plt

x = [2, 6, 15]
y = [20, 9, 15]

x_error = [2, 5.1, 1]

plt.bar(x,y)
plt.errorbar(x, y, xerr = x_error,ecolor = 'maroon',color='red')

plt.show()
```

