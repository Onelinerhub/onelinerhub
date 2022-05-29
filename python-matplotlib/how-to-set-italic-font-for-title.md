# How to set italic font for title

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.title('Example', style='italic')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `title` - set chart title
- `style='italic'` - change font style to `italic`
- `.show()` - render chart in a separate window

group: font_italic

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.title('Example', style='italic')

plt.show()
```

