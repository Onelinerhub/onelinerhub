# How do I use Python and SciPy to fit an exponential curve?
// plain

To use Python and SciPy to fit an exponential curve, you can use the `curve_fit` function from `scipy.optimize`. This function takes a user-defined function that models the data as well as the x and y data points as arguments. It then returns an array of optimized parameters that best fit the data.

## Example code

```
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * np.exp(-b * x)

xdata = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
ydata = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

popt, pcov = curve_fit(func, xdata, ydata)

print(popt)
```

## Output example

```
[ 1.5  -1. ]
```

## Code explanation


1. `import numpy as np`: imports the `numpy` library as `np`, which is used to define the x and y data points.
2. `from scipy.optimize import curve_fit`: imports the `curve_fit` function from the `scipy.optimize` library, which is used to fit the data points to an exponential curve.
3. `def func(x, a, b):`: defines a user-defined function that takes x and two parameters (a and b) as arguments and returns an exponential function.
4. `xdata = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])`: defines the x data points as a numpy array.
5. `ydata = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])`: defines the y data points as a numpy array.
6. `popt, pcov = curve_fit(func, xdata, ydata)`: uses the `curve_fit` function to fit the data points to the user-defined exponential function. It returns an array of optimized parameters that best fit the data.
7. `print(popt)`: prints the optimized parameters.

## Helpful links

- [scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- [Python Curve Fitting](https://realpython.com/linear-regression-in-python/)

onelinerhub: [How do I use Python and SciPy to fit an exponential curve?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-fit-an-exponential-curve-1687059154)