# How to set bar color

```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12], color=['blue','red','#48A48A'])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `['UA', 'UK', 'USA']` - x-axis values
- `[10, 11, 12]` - y-axis values
- `color=` - specify colors array for bars
- `blue` - first bar [named color](https://matplotlib.org/stable/gallery/color/named_colors.html)
- `red` - second bar [named color](https://matplotlib.org/stable/gallery/color/named_colors.html)
- `#48A48A` - third bar color (can be HEX code)

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12], color=['blue','red','#AAA999'])
plt.show()
```

