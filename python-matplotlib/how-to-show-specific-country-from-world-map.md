# How to show specific country from world map

```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world[world.country=='Ukraine'].plot()

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import geopandas` - loads [lib:GeoPandas module](/python-matplotlib/how-to-install-geopandas-module) to work with maps and geo charts
- `.read_file(` - reads map file
- `naturalearth_lowres` - sample world map file to use
- `world.continent` - filters world map based on a specified continent
- `.show()` - render chart in a separate window

group: map

## Example: 
```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world[world.country=='Ukraine'].plot()

plt.show()
```

