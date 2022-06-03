# 3D Scatter chart example

```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(1, 1, 1)
ax.scatter(2, 2, 1)
ax.scatter(2, 3, 0)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.add_subplot` - create sub chart
- `projection='3d'` - set 3d mode for this chart
- `.scatter(` - plots a point chart
- `.show()` - render chart in a separate window

group: scatter

## Example: 
```python
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(1, 1, 1)
ax.scatter(2, 2, 1)
ax.scatter(2, 3, 0)

plt.show()
```

