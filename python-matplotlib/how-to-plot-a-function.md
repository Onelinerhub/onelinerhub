# How to plot a function

### In order to plot a function (defined with `def`) we can easily use [`Numpy`](/python-numpy):

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 2*x*x - 3*x + 7

x = np.linspace(-10, 10, 30)

plt.plot(x, f(x))

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `def f(x)` - defined function we need to plot
- `np.linspace` - generate random values based on specified range and count 
- `.plot(` - plot specified data
- `x, f(x)` - use `x` array for `X-axis` and `f(x)` values (will be automatically calculated by `Numpy`) for `Y-axis`
- `.show()` - render chart in a separate window

## Example: 
```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 2*x*x - 3*x + 7

x = np.linspace(-10, 10, 30)

plt.plot(x, f(x))

plt.show()
```

