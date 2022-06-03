# How to change legend position

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend(loc='lower right')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `label` - set label for this line
- `.legend(` - show and configure legend (we use default configuration in our case)
- `loc=` - configure legend location
- `lower right` - show legend in the `lower right` corner, see [available values](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)

group: legend

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend(loc='lower right')
plt.show()
```

