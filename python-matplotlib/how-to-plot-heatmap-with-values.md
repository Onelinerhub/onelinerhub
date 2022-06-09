# How to plot heatmap with values

```python
import matplotlib.pyplot as plt

data = [[0.8, 2.4, 2.5], [1.3, 1.2, 0.0], [0.1, 2.0, 0.0]]
fig, ax = plt.subplots()
im = ax.imshow(data)

for i in range(len(data)):
  for j in range(len(data[0])):
    text = ax.text(j, i, data[i][j])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `.imshow(` - displays data as an image (used for heatmaps from 2d arrays)
- `for i in range(len(data))` - iterate through data rows
- `for j in range(len(data[0]))` - iterate through data columns
- `.text(` - adds custom text to chart
- `j, i, data[i][j]` - add data value as a text object using corresponding coordinates
- `.show()` - render chart in a separate window

group: heatmap

## Example: 
```python
import matplotlib.pyplot as plt

data = [[0.8, 2.4, 2.5], [1.3, 1.2, 0.0], [0.1, 2.0, 0.0]]
fig, ax = plt.subplots()
im = ax.imshow(data)

for i in range(len(data)):
  for j in range(len(data[0])):
    text = ax.text(j, i, data[i][j])

plt.show()
```

