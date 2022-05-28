# How to draw 45° line

```python
import matplotlib.pyplot as plt
plt.axline([0,0], [1,1])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `axline` - draws a line based on 2 points
- `[0,0]` - first point
- `[1,1]` - second point
- `.show()` - render chart in a separate window

group: line_std

## Example: 
```python
import matplotlib.pyplot as plt
plt.axline([0,0], [1,1])
plt.show()
```

