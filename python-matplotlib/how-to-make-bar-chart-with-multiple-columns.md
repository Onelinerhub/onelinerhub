# How to make bar chart with multiple columns

### See how you can [plot 3 or more bar columns using Numpy](/python-matplotlib/how-to-make-bar-chart-with-multiple-columns-using-numpy).

```python
import matplotlib.pyplot as plt
x = [1,2,3]
plt.bar(x, [10, 11, 12], label='coolness', width=0.4, align='edge')
plt.bar(x, [90, 85, 88], label='friendness', width=-0.4, align='edge')
plt.xticks(x, ['UA', 'UK', 'USA'])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.bar` - will plot bar chart
- `['UA', 'UK', 'USA']` - x-axis labels
- `[10, 11, 12]` - y-axis values of a second column of each bar
- `[90, 85, 88]` - y-axis values of a first column of each bar
- `width=0.4, align='edge'` - draw this bar column at 40% width and aligned to the right
- `width=-0.4, align='edge'` - draw this bar column at 40% width and aligned to the left (since width is negative)
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
x = [1,2,3]
plt.bar(x, [10, 11, 12], label='coolness', width=0.45, align='edge')
plt.bar(x, [90, 85, 88], label='friendness', width=-0.45, align='edge')
plt.xticks(x, ['UA', 'UK', 'USA'])
plt.show()
```

