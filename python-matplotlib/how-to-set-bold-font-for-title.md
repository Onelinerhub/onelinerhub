# How to set bold font for title

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.title('Example', weight='bold')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `title` - set chart title
- `weight` - set weight of text (`bold` in our case)
- `.show()` - render chart in a separate window

group: font_bold

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.title('Example', weight='bold')

plt.show()
```

