# How to put grid lines below chart

```python
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.grid()
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `plt.rc` - configure chart object
- `axisbelow=True` - put axes objects (including grid) below chart figures
- `.bar` - will plot bar chart
- `.grid(` - add and configure grid
- `.show()` - render chart in a separate window

group: grid

## Example: 
```python
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.grid()
plt.show()
```

