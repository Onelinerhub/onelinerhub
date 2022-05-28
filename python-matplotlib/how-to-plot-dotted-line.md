# How to plot dotted line

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], ':')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `[1,2,10,6,15,3,4]` - values to use for first line
- `'--'` - use dashed [line style](https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html)
- `.show()` - render chart in a separate window

group: line

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], ':')
plt.show()
```

