# How do I use Python Scipy to fit a curve?
// plain

To use Python Scipy to fit a curve, you need to use the `curve_fit` function from the `scipy.optimize` package. This function takes a function that describes the curve you want to fit, and the data points you are fitting to.

## Example code

```
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a * np.exp(-b * x)

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3)
ydata = y + 0.2 * np.random.normal(size=len(xdata))

popt, pcov = curve_fit(func, xdata, ydata)
```

The output of this code is the optimized parameters `popt` and the covariance of the parameters `pcov`.

## Code explanation

- `from scipy.optimize import curve_fit`: imports the `curve_fit` function from the `scipy.optimize` package
- `def func(x, a, b):`: defines the function that describes the curve you want to fit
- `xdata = np.linspace(0, 4, 50)`: creates an array of x-values for the data points
- `y = func(xdata, 2.5, 1.3)`: creates an array of y-values calculated from the function with the given parameters
- `ydata = y + 0.2 * np.random.normal(size=len(xdata))`: adds random noise to the y-values to simulate real data points
- `popt, pcov = curve_fit(func, xdata, ydata)`: calls the `curve_fit` function to optimize the parameters of the function

## Helpful links
- [Scipy curve_fit documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- [Python Scipy tutorial](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html)

onelinerhub: [How do I use Python Scipy to fit a curve?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-fit-a-curve)