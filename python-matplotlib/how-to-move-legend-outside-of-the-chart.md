# How to move legend outside of the chart

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')

h, l = plt.gca().get_legend_handles_labels()
plt.legend(loc='center right', bbox_to_anchor=(1, 0.5))

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `label` - set label for this line
- `get_legend_handles_labels` - returns legend labels and handlers
- `.legend(` - show and configure legend (we use default configuration in our case)
- `[h[1], h[0]], [l[1], l[0]]` - we pass legend handles and labels in reverse order to reverse order
- `.show()` - render chart in a separate window

group: legend

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')

h, l = plt.gca().get_legend_handles_labels()
plt.legend(loc=(1, 1))

plt.show()
```

