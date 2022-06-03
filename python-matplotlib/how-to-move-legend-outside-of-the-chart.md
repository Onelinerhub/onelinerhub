# How to move legend outside of the chart

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')

h, l = plt.gca().get_legend_handles_labels()
plt.legend(loc=(0, 1.05),ncol=2)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `label` - set label for this line
- `get_legend_handles_labels` - returns legend labels and handlers
- `.legend(` - show and configure legend
- `loc=` - configure legend location, we can pass coordinates tuple here 
- `(0, 1.05)` - place our legend in the top left corner a little higher than the chart top border
- `ncol=2` - used to render legend labels horizontally
- `.show()` - render chart in a separate window

group: legend

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')

h, l = plt.gca().get_legend_handles_labels()
plt.legend(loc=(0, 1.05),ncol=2)

plt.show()
```

