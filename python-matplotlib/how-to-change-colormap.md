# How to set colormap

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(30, 30)

plt.pcolormesh(data, cmap='magma', rasterized=True, vmin=-4, vmax=4)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.random.randn(30, 30)` - generate random matrix `30x30` in size
- `pcolormesh` - create [pseudo color plot](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.pcolormesh.html)
- `cmap` - set [colormap](https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html) to use
- `.show()` - render chart in a separate window

group: colormap

## Example: 
```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(30, 30)

plt.pcolormesh(data, cmap='magma', rasterized=True, vmin=-4, vmax=4)
plt.show()
```

