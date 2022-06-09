# How to fill countries with colors using world map

```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world.plot()

world[world.name == 'Ukraine'].plot(color='yellow',ax=ax)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import geopandas` - loads [lib:GeoPandas module](/python-matplotlib/how-to-install-geopandas-module) to work with maps and geo charts
- `world.plot()` - plots world map
- `.read_file(` - reads map file
- `naturalearth_lowres` - sample world map file to use
- `world.name == 'Ukraine'` - set specific country to plot
- `color='yellow'` - plot specific country with `yellow` color
- `ax=ax` - we want to plot our country on an already existing plot (referred by `ax` object)
- `.show()` - render chart in a separate window

group: map

## Example: 
```python
import matplotlib.pyplot as plt
import geopandas

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world.plot()

world[world.name == 'Ukraine'].plot(color='yellow',ax=ax)

plt.show()
```

