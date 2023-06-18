# How do I use Python and SciPy to fit an exponential curve?
// plain

To fit an exponential curve with Python and SciPy, the `curve_fit` function from `scipy.optimize` can be used.

The `curve_fit` function takes a function with the desired curve shape as an argument, as well as the data points to fit the curve to.

For example, to fit an exponential curve to data points `xdata` and `ydata`:

```
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

popt, pcov = curve_fit(func, xdata, ydata)
```

The `popt` variable contains the best-fit parameters for the curve, and `pcov` contains the covariance of the parameters.

Parts of the code:
- `from scipy.optimize import curve_fit`: imports the `curve_fit` function from SciPy
- `import numpy as np`: imports the NumPy library
- `def func(x, a, b, c):`: defines the function for the exponential curve, with parameters `a`, `b`, and `c`
- `popt, pcov = curve_fit(func, xdata, ydata)`: uses `curve_fit` to fit the data points to the defined exponential curve

## Helpful links
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
- https://docs.scipy.org/doc/numpy/reference/

onelinerhub: [How do I use Python and SciPy to fit an exponential curve?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-fit-an-exponential-curve)