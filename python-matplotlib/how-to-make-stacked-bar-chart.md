# How to make stacked bar chart

```python
import matplotlib.pyplot as plt
x = [1,2,3]
a = [10, 21, 42]
b = [90, 85, 88]
plt.bar(x, a)
plt.bar(x, b, bottom = a)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `[1,2,3]` - x-axis values
- `a = [10, 21, 42]` - first part of stacked bars
- `b = [90, 85, 88]` - second part of stacked bars
- `.bar` - will plot bar chart
- `bottom = a` - we ask Python to draw second bars (`b`) starting from previous bars values (`a`) instead of zero baseline
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
x = [1,2,3]
a = [10, 21, 42]
b = [90, 85, 88]
plt.bar(x, a)
plt.bar(x, b, bottom = a)
plt.show()
```

