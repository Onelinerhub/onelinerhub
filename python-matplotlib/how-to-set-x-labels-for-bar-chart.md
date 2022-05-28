# How to set x labels for bar chart

```python
import matplotlib.pyplot as plt
plt.bar([1,2,3], [10, 11, 12])
plt.xticks([1,2,3], ['UA', 'UK', 'USA'])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `[1,2,3]` - x-axis values
- `[10, 11, 12]` - y-axis values
- `xticks` - set specified labels for x-axis
- `['UA', 'UK', 'USA']` - labels to use for x axis

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
plt.bar([1,2,3], [10, 11, 12])
plt.xticks([1,2,3], ['UA', 'UK', 'USA'])
plt.show()
```

