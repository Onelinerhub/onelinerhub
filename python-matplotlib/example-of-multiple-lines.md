# Example of multiple lines

### Plotting multiple lines is as simple as calling `plt.plot()` method multiple times:

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4])
plt.plot([4,2,11,2,1,20,25])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `[1,2,10,6,15,3,4]` - values to use for first line
- `[4,2,11,2,1,20,25]` - values to use for second line
- `.show()` - render chart in a separate window

group: line

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4])
plt.plot([4,2,11,2,1,20,25])
plt.show()
```

