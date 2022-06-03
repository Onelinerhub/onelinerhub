# How to zoom in chart

```python
import matplotlib.pyplot as plt

plt.margins(-0.1, -0.1)
plt.plot([3,2,4,5,6,1,1,4])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.margins(` - set chart margins to simulate zooming
- `-0.1, -0.1` - zooms in when those values are negative
- `.show()` - render chart in a separate window

group: zoom

## Example: 
```python
import matplotlib.pyplot as plt

plt.margins(-0.1, -0.1)
plt.plot([3,2,4,5,6,1,1,4])
plt.show()
```

