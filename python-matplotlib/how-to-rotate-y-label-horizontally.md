# How to rotate Y label horizontally

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.ylabel("Y", rotation=0)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `xlabel` - set label for x-axis
- `ylabel` - set label for y-axis
- `.show()` - render chart in a separate window

group: label

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.ylabel("Y", rotation=0)

plt.show()
```

