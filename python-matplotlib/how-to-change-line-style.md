# How to change line style

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], 'go--')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `[1,2,10,6,15,3,4]` - values to use as data
- `go--` - define [line style](https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html): `g` - green color, `o` - circle marker, `--` - dashed line style
- `.show()` - render chart in a separate window

group: line

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], 'go--')
plt.show()
```

