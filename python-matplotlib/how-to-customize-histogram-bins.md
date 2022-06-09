# How to customize histogram bins

```python
import matplotlib.pyplot as plt

x = [1,2,5,1,2,3,5,6,7,4,2,2,4,5,6]
plt.hist(x,bins=3)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.hist(` - plots histogram for specified data
- `bins` - number of histogram bins (bars) to group data into
- `.show()` - render chart in a separate window

group: histogram

## Example: 
```python
import matplotlib.pyplot as plt

x = [1,2,5,1,2,3,5,6,7,4,2,2,4,5,6]
plt.hist(x,bins=3)
plt.show()
```

