# How to add multiple plots on a single figure

### You can add multiple plots by calling plotting methods (e.g. `plot()`, `bar()`,...) multiple times:

```python
import matplotlib.pyplot as plt

plt.bar(['a', 'b', 'c'], [3,4,2])
plt.plot([4,9,6])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `.plot(` - will plot line chart
- `.show()` - render chart in a separate window

group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

plt.bar(['a', 'b', 'c'], [3,4,2])
plt.plot([4,9,6])

plt.show()
```

