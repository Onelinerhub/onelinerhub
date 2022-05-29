# How to set italic font for labels

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel('X', style='italic')
plt.ylabel('Y', style='italic')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `xlabel` - set label for x-axis
- `ylabel` - set label for y-axis
- `style='italic'` - use `italic` font style
- `.show()` - render chart in a separate window

group: font_italic

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel('X', style='italic')
plt.ylabel('Y', style='italic')

plt.show()
```

