# How to change figure title

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
fig.suptitle('I am figure title')

axs[0].plot([2,1,5,2,3])
axs[0].set_title('first line')

axs[1].plot([4,2,4,6,1])
axs[1].set_title('second line')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `.suptitle(` - sets figure (chart area) title
- `.plot(` - plot specified data
- `.set_title(` - sets given chart (subplot) title
- `.show()` - render chart in a separate window

group: figure

## Example: 
```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
fig.suptitle('I am figure title')

axs[0].plot([2,1,5,2,3])
axs[0].set_title('first line')

axs[1].plot([4,2,4,6,1])
axs[1].set_title('second line')

plt.show()
```

