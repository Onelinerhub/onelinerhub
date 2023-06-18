# How do I use scipy.optimize.curve_fit in Python?
// plain

`scipy.optimize.curve_fit` is a function in the SciPy library of Python used to fit a curve of the form `f(x, *params)` to data. It finds the parameters of the curve that best fit the given data points.

```
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a*x + b

x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1, 3, 5, 7, 9, 11])

popt, pcov = curve_fit(func, x_data, y_data)

print(popt)
```

## Output example

```
[2. 1.]
```

The code above uses `curve_fit` to fit a linear function `f(x) = a*x + b` to the given data points. The `func` function is defined as the model to fit the data to. The `x_data` and `y_data` are the x-coordinates and y-coordinates of the data points. The `curve_fit` function returns two values, `popt` and `pcov` which are the optimal parameters and the covariance matrix of the parameters respectively. In this case, the optimal parameters are `a = 2` and `b = 1`.

## Code explanation

1. `from scipy.optimize import curve_fit`: imports the `curve_fit` function from the SciPy library
2. `import numpy as np`: imports the NumPy library for array manipulation
3. `def func(x, a, b)`: defines the model function to fit the data to
4. `x_data` and `y_data`: the x-coordinates and y-coordinates of the data points
5. `popt, pcov = curve_fit(func, x_data, y_data)`: calls the `curve_fit` function to fit the data to the model function
6. `print(popt)`: prints the optimal parameters

## Helpful links
1. https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
2. https://www.tutorialspoint.com/scipy/scipy_optimize.htm

onelinerhub: [How do I use scipy.optimize.curve_fit in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-scipy-optimize-curve-fit-in-python)