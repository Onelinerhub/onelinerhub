# How to plot Numpy data

### We cam pass [`Numpy`](/python-numpy) arrays directly to `plot()` method:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 15, 50)

plt.plot(x, x**2)

plt.show()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `np.linspace` - generate random values based on specified range and count
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

## Example: 
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 15, 50)

plt.plot(x, x**2)

plt.show()
```

