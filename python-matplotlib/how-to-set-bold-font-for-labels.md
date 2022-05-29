# How to set bold font for labels

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel('X', weight='bold')
plt.ylabel('Y', weight='bold')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `xlabel` - set label for x-axis
- `ylabel` - set label for y-axis
- `weight='bold'` - set font style to `bold`
- `.show()` - render chart in a separate window

group: font_style

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel('X', weight='bold')
plt.ylabel('Y', weight='bold')

plt.show()
```

