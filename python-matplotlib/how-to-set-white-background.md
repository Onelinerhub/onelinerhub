# How to set white background

```bash
import matplotlib.pyplot as plt
plt.figure().patch.set_facecolor('white')
plt.axes().set_facecolor('white')
plt.plot([2,1,2,2])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `set_facecolor` - sets object background
- `white` - set white background for both chart and general plot area
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

## Example: 
```bash
import matplotlib.pyplot as plt
plt.figure().patch.set_facecolor('white')
plt.axes().set_facecolor('white')
plt.plot([2,1,2,2])
plt.show()
```

