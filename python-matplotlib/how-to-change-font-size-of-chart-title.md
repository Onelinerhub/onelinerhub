# How to change font size of chart title

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.title('hello big', fontsize=20)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `title` - set chart title
- `hello big` - text to use as title
- `fontsize` - set chart title font size
- `.show()` - render chart in a separate window

group: font_size

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.title('hello big', fontsize=25)
plt.show()
```

