# How to plot multiple bars on the same chart

### In order to plot multiple lines, you simply call `bar()` method multiple times ([another multiple bar charts example](/python-matplotlib/how-to-make-bar-chart-with-multiple-columns)):

```python
import matplotlib.pyplot as plt

plt.bar(['a', 'b', 'c'], [3,4,2])
plt.bar(['a', 'b', 'c'], [1,2,1], width=0.4)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `width=0.4` - change width for second bar chart, so we can see both charts
- `.show()` - render chart in a separate window

group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

plt.bar(['a', 'b', 'c'], [3,4,2])
plt.bar(['a', 'b', 'c'], [1,2,1], width=0.4)

plt.show()
```

