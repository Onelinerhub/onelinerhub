# How to set x-axis label for bar chart

```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.xlabel('Coolness of the country')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `['UA', 'UK', 'USA']` - x-axis values
- `[10, 11, 12]` - y-axis values
- `xlabel` - set label for x-axis
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.xlabel('Coolness of the country')
plt.show()
```

