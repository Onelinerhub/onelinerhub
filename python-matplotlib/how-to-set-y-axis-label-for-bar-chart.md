# How to set y-axis label for bar chart

```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.ylabel('Coolness of the country')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `['UA', 'UK', 'USA']` - x-axis values
- `[10, 11, 12]` - y-axis values
- `ylabel` - set label for y-axis
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.ylabel('Coolness of the country')
plt.show()
```

