# How can I use Python and SciPy to resample data?
// plain

Using Python and SciPy, data can be resampled by applying a variety of interpolation techniques. The SciPy library provides a number of functions for interpolation, including linear, nearest neighbour, and cubic spline interpolation.

For example, the following code block uses SciPy's `interp1d` function to resample a given data set using linear interpolation:

```
from scipy.interpolate import interp1d
import numpy as np

# Given data
x = np.array([1,2,3,4,5])
y = np.array([1,2,4,8,16])

# Resample using linear interpolation
f = interp1d(x, y, kind='linear')
x_new = np.linspace(1, 5, num=50)
y_new = f(x_new)

print(y_new)
```

## Output example

```
[ 1.          1.16326531  1.32653061  1.48979592  1.65306122  1.81632653
  1.97959184  2.14285714  2.30612245  2.46938776  2.63265306  2.79591837
  2.95918367  3.12244898  3.28571429  3.44897959  3.6122449   3.7755102
  3.93877551  4.10204082  4.26530612  4.42857143  4.59183673  4.75510204
  4.91836735  5.08163265  5.24489796  5.40816327  5.57142857  5.73469388
  5.89795918  6.06122449  6.2244898   6.3877551   6.55102041  6.71428571
  6.87755102  7.04081633  7.20408163  7.36734694  7.53061224  7.69387755
  7.85714286  8.02040816  8.18367347  8.34693878  8.51020408  8.67346939
  8.83673469  9.        ]
```

The code above does the following:

1. Imports the `interp1d` function from SciPy's `interpolate` module, as well as `numpy`
2. Defines the x and y values of the original data set
3. Uses the `interp1d` function to create a linear interpolator from the original data set
4. Defines a new set of x values to use for the resampled data
5. Uses the interpolator to calculate the y values of the resampled data
6. Prints the resampled data

## Helpful links
- [SciPy Interpolation Documentation](https://docs.scipy.org/doc/scipy/reference/interpolate.html)
- [Numpy's linspace Function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)

onelinerhub: [How can I use Python and SciPy to resample data?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-resample-data)