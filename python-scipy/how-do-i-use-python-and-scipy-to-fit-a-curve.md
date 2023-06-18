# How do I use Python and SciPy to fit a curve?
// plain

To fit a curve with Python and SciPy, you can use the `curve_fit` function from the `scipy.optimize` module. This function takes a function that you want to fit to the data, as well as the x and y data. It then returns the parameters of the fitted curve.

For example:

```
from scipy.optimize import curve_fit
import numpy as np

# Define function to fit
def func(x, a, b):
    return a * np.exp(-b * x)

# Generate data
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3)
ydata = y + 0.2 * np.random.normal(size=len(xdata))

# Fit
popt, pcov = curve_fit(func, xdata, ydata)

print(popt)
# Output: [2.55423706 1.35190947]
```

The `curve_fit` function returns an array of parameters, `popt`, that can be used to generate a fitted curve.

Parts of the code:
- `from scipy.optimize import curve_fit`: imports the `curve_fit` function from the `scipy.optimize` module
- `def func(x, a, b):`: defines the function to fit to the data
- `xdata = np.linspace(0, 4, 50)`: creates an array of x values
- `ydata = y + 0.2 * np.random.normal(size=len(xdata))`: creates an array of y values with noise
- `popt, pcov = curve_fit(func, xdata, ydata)`: fits the function to the data
- `print(popt)`: prints the parameters of the fitted curve

## Helpful links
- [Scipy curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- [Numpy linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)
- [Numpy random normal](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html)

onelinerhub: [How do I use Python and SciPy to fit a curve?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-fit-a-curve)