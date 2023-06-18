# How can I use Python SciPy to fit a model?
// plain

Using the Python SciPy package, you can fit a model to data by using the `curve_fit` function. This function takes a function that describes the model, an array of x-values, and an array of y-values, and returns an array of parameters that best fit the data. For example,

```
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * x + b

xdata = [0, 1, 2]
ydata = [0, 1, 2]

popt, pcov = curve_fit(func, xdata, ydata)

print(popt)
```

The above code would output `[1.0, 0.0]` as the parameters that best fit the data.

## Code explanation

- `from scipy.optimize import curve_fit`: imports the `curve_fit` function from the SciPy package
- `def func(x, a, b):`: defines the model function with two parameters, `a` and `b`
- `xdata = [0, 1, 2]` and `ydata = [0, 1, 2]`: defines the x- and y-values to fit the model to
- `popt, pcov = curve_fit(func, xdata, ydata)`: calls `curve_fit` to fit the model to the data
- `print(popt)`: prints the best-fit parameters

## Helpful links
- [SciPy Optimize Curve Fitting](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)

onelinerhub: [How can I use Python SciPy to fit a model?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-fit-a-model)