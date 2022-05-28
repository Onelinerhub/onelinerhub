# How to make horizontal bar chart

```python
import matplotlib.pyplot as plt
plt.barh(['UA', 'UK', 'USA'], [10, 11, 12])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.barh` - will plot horizontal bar chart
- `['UA', 'UK', 'USA']` - vertical axis values (labels)
- `[10, 11, 12]` - horizontal axis values
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
plt.barh(['UA', 'UK', 'USA'], [10, 11, 12])
plt.show()
```

