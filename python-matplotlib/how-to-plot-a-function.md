# How to plot a function

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 2*x*x - 3*x + 7

x = np.linspace(-10, 10, 30)

plt.plot(x, f(x))

plt.show()
```


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

