# How do I use Python and SciPy for interpolation?
// plain

Python and SciPy can be used to interpolate data by fitting a function to the existing data points. The SciPy library provides many functions for interpolation such as `interp1d`, `UnivariateSpline`, and `InterpolatedUnivariateSpline`.

For example, to interpolate a linear function using `interp1d`, we can use the following code:

```
from scipy.interpolate import interp1d
import numpy as np

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)

import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
```

## Output example


![alt text](https://i.stack.imgur.com/QQj3Y.png)

The code above:

1. Imports the `interp1d` function from the `scipy.interpolate` library and the `numpy` library as `np`
2. Creates `x` and `y` arrays of data points
3. Uses the `interp1d` function to create a linear interpolation function `f` and a cubic interpolation function `f2`
4. Creates a new array of data points `xnew`
5. Plots the original data points, the linear interpolation, and the cubic interpolation

## Helpful links

- https://docs.scipy.org/doc/scipy/reference/interpolate.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html

onelinerhub: [How do I use Python and SciPy for interpolation?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-for-interpolation)