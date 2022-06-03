# How to write text on plot

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,6,2])
plt.text(1, 3.5, "hi from python")

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.text(` - adds custom text to chart
- `1, 3.5` - vertical and horizontal coordinates for our text box
- `hi from python` - sample text to show
- `.show()` - render chart in a separate window

group: text

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3,6,2])
plt.text(1, 3.5, "hi from python")

plt.show()
```

