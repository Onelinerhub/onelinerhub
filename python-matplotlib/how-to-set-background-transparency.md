# How to set background transparency

```python
import matplotlib.pyplot as plt

p = plt.figure().patch
p.set_facecolor('orange')
p.set_alpha(0.5)

ax = plt.axes()
ax.patch.set_facecolor('red')
ax.patch.set_alpha(0.25)

plt.plot([2,1,2,2])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `set_facecolor` - sets object background
- `set_alpha` - set object background transparency
- `plt.figure()` - object to manipulate general area
- `plt.axes()` - object to manipulate chart
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

group: background

## Example: 
```python
import matplotlib.pyplot as plt

p = plt.figure().patch
p.set_facecolor('orange')
p.set_alpha(0.5)

ax = plt.axes()
ax.patch.set_facecolor('red')
ax.patch.set_alpha(0.25)

plt.plot([2,1,2,2])
plt.show()
```

