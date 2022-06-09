# How to plot dots on a world map

```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()

plt.scatter([-87,-88,-29],[21,41,-4],s=200,c='red')

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import geopandas` - loads [lib:GeoPandas module](/python-matplotlib/how-to-install-geopandas-module) to work with maps and geo charts
- `world.plot()` - plots world map
- `.read_file(` - reads map file
- `naturalearth_lowres` - sample world map file to use
- `.scatter(` - plots a point chart
- `[-87,-88,-29]` - list of longitudes
- `[21,41,-4]` - list of latitudes
- `.show()` - render chart in a separate window

group: map

## Example: 
```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()

plt.scatter([-87,-88,-29],[21,41,-4],s=200,c='red')

plt.show()
```

