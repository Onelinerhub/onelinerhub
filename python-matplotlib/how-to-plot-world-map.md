# How to plot world map

```python
import matplotlib.pyplot as plt
import geopandas

world.plot()

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import geopandas` - loads [GeoPandas module](/python-matplotlib/how-to-plot-world-map) to work with maps and geo charts
- `world.plot()` - plots world map
- `.show()` - render chart in a separate window

group: map

## Example: 
```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()

plt.show()
```

