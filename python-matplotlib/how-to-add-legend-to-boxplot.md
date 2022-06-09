# How to add legend to boxplot

```python
import matplotlib.pyplot as plt

plt.boxplot([2,3,6,2,4,5,1,10])
 
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.boxplot(` - plots `boxplot` (features of a given set of values: minimum, first quartile, median, third quartile and maximum)
- `.show()` - render chart in a separate window

group: boxplot

## Example: 
```python
import matplotlib.pyplot as plt

plt.boxplot([[2,3,6,2,4,5,1,2], [4,5,7,17,3]])
plt.legend(['a', 'b'])

plt.show()
```

