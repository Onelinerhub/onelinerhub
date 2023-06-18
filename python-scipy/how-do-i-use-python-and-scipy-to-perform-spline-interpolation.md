# How do I use Python and SciPy to perform spline interpolation?
// plain

Spline interpolation is a method of constructing new data points within the range of a discrete set of known data points. Python and SciPy provide a convenient set of functions for performing spline interpolation.

## Example code

```
import numpy as np
from scipy.interpolate import interp1d

# Create a set of data points
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)

# Create a linear interpolation function
f = interp1d(x, y)

# Interpolate at new points
xnew = np.linspace(0, 10, num=41, endpoint=True)
ynew = f(xnew)
```

The code above creates a set of data points `x` and `y` and then creates a linear interpolation function `f` using `interp1d`. The function `f` is then used to interpolate at new points `xnew` and `ynew`.

## Code explanation

1. `import numpy as np`: imports the NumPy library as `np`
2. `from scipy.interpolate import interp1d`: imports the `interp1d` function from the SciPy library
3. `x = np.linspace(0, 10, num=11, endpoint=True)`: creates a set of data points `x` between 0 and 10 with 11 points
4. `y = np.cos(-x**2/9.0)`: creates a set of data points `y` for each `x` point using the cosine function
5. `f = interp1d(x, y)`: creates a linear interpolation function `f` using `interp1d`
6. `xnew = np.linspace(0, 10, num=41, endpoint=True)`: creates a set of new points `xnew` between 0 and 10 with 41 points
7. `ynew = f(xnew)`: uses the linear interpolation function `f` to interpolate at the new points `xnew` and creates a set of new points `ynew`

## Helpful links
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/)

onelinerhub: [How do I use Python and SciPy to perform spline interpolation?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-perform-spline-interpolation)