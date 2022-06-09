# How to add third Y axis

### In order to add multiple `Y` axes, we need to call `twinx()` method multiple times and adjust `Y` axes positions:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
twin1 = ax.twinx()
twin2 = ax.twinx()

twin2.spines.right.set_position(("axes", 1.05))

p1, = ax.plot([0, 1, 2], "g-")
p2, = twin1.plot([1, 7, 5], "r-")
p3, = twin2.plot([4, 2, 3], "b-")

ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
twin1.set_ylim(0, 8)
twin2.set_ylim(0, 4)

ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `twinx()` - creates twin axes sharing `x` axis
- `twin2.spines.right.set_position` - reposition second `Y` axis so they will not overlap
- `ax.plot(` - plot first line (green one)
- `twin1.plot(` - plot second line
- `twin2.plot(` - plot third line
- `.set_xlim(` - set `x` axis range
- `.set_ylim(` - set `y` axis range
- `.show()` - render chart in a separate window

group: multiple_y

## Example: 
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
twin1 = ax.twinx()
twin2 = ax.twinx()

twin2.spines.right.set_position(("axes", 1.05))

p1, = ax.plot([0, 1, 2], "g-")
p2, = twin1.plot([1, 7, 5], "r-")
p3, = twin2.plot([4, 2, 3], "b-")

ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
twin1.set_ylim(0, 8)
twin2.set_ylim(0, 4)

ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())

plt.show()
```

