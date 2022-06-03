# Scatter chart example

```python
import matplotlib.pyplot as plt

plt.scatter([1,2,3],[2,2,2])
plt.scatter(2,1,s=600)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.scatter(` - plots a point chart
- `[1,2,3]` - list of `x` coordinates
- `[2,2,2]` - list of `y` coordinates
- `2,1` - `x` and `y` coordinates
- `s=600` - point size
- `.show()` - render chart in a separate window

## Example: 
```python
import matplotlib.pyplot as plt

plt.scatter([1,2,3],[2,2,2])
plt.scatter(2,1,s=600)

plt.show()
```

