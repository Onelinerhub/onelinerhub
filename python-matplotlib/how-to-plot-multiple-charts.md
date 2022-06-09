# How to plot multiple charts

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0][0].plot([1,3,2])
axes[0][1].plot([8,2,5])
axes[1][0].plot([3,4,6,2,4,4,5,4,6])
axes[1][1].bar(['a','b','c'],[4,2,6])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `nrows` - number of charts vertically (rows)
- `ncols` - number of charts horizontally (cols)
- `axes` - matrix (2-dimensional array) of charts (`2x2` in our case) available to plot something
- `.plot(` - plots line chart
- `.bar` - plots bar chart
- `.show()` - render chart in a separate window

group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

fig = plt.figure()
fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0][0].plot([1,3,2])
axes[0][1].plot([8,2,5])
axes[1][0].plot([3,4,6,2,4,4,5,4,6])
axes[1][1].bar(['a','b','c'],[4,2,6])

plt.show()
```

