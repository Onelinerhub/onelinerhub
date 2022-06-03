# How to locate labels horizontally in legend

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend(ncol=2)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `label` - set label for this line
- `.legend(` - show and configure legend
- `ncol` - configure number of columns to place labels into (we use `2` because we have 2 labels)
- `.show()` - render chart in a separate window

group: legend

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend(ncol=2)
plt.show()
```

