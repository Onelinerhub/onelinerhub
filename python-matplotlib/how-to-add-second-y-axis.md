# How to add second Y axis

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
twin = ax.twinx()

p1, = ax.plot([0, 1, 2], "g-")
p2, = twin.plot([1, 7, 5], "r-")

ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
twin.set_ylim(0, 8)

ax.tick_params(axis='y', colors=p1.get_color())
twin.tick_params(axis='y', colors=p2.get_color())

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](/python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `twinx()` - creates twin axes sharing `x` axis
- `ax.plot(` - plot first line (green one)
- `twin.plot(` - plot second line (red one)
- `.set_xlim(` - set `x` axis range
- `.set_ylim(` - set `y` axis range
- `.show()` - render chart in a separate window

group: multiple_y

## Example: 
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
twin = ax.twinx()

p1, = ax.plot([0, 1, 2], "g-")
p2, = twin.plot([1, 7, 5], "r-")

ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
twin.set_ylim(0, 8)

ax.tick_params(axis='y', colors=p1.get_color())
twin.tick_params(axis='y', colors=p2.get_color())

plt.show()
```

