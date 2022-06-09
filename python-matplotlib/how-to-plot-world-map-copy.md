# How to plot points on a world map

```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import geopandas` - loads [lib:GeoPandas module](/python-matplotlib/how-to-install-geopandas-module) to work with maps and geo charts
- `world.plot()` - plots world map
- `.read_file(` - reads map file
- `naturalearth_lowres` - sample world map file to use
- `.show()` - render chart in a separate window

group: map

## Example: 
```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()

plt.scatter([-87,-88,-89],[41,41,41],s=200)

plt.show()
```

