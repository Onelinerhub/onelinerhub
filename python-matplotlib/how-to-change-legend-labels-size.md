# How to change legend labels size

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend(prop={'size': 20})
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `label` - set label for this line
- `.legend(` - show and configure legend
- `prop` - set labels properties
- `size` - specify font size to use for labels
- `.show()` - render chart in a separate window

group: legend

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend(prop={'size': 20})
plt.show()
```

