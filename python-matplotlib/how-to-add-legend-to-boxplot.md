# How to change boxplot colors

```python
import matplotlib.pyplot as plt

bp = plt.boxplot([[2,3,6,2,4,5,1,2], [4,5,7,17,3]], notch=True, patch_artist=True)

bp['boxes'][0].set_facecolor('red')
bp['boxes'][0].set_color('red')
bp['boxes'][1].set_facecolor('green')
bp['boxes'][1].set_color('green')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.boxplot(` - plots `boxplot` (features of a given set of values: minimum, first quartile, median, third quartile and maximum)
- `set_facecolor` - sets box background
- `set_color` - set boxplot line color
- `.show()` - render chart in a separate window

group: boxplot

## Example: 
```python
import matplotlib.pyplot as plt

bp = plt.boxplot([[2,3,6,2,4,5,1,2], [4,5,7,17,3]], notch=True, patch_artist=True)

bp['boxes'][0].set_facecolor('red')
bp['boxes'][0].set_color('red')
bp['boxes'][1].set_facecolor('green')
bp['boxes'][1].set_color('green')

plt.show()
```

