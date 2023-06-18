# How can I use Python and SciPy to perform numerical integration?
// plain

Python and SciPy can be used to perform numerical integration with the `scipy.integrate` sub-package. The `scipy.integrate.quad` function is a general purpose function for numerical integration of a function of one variable over a given fixed range.

For example, to integrate the function `f(x) = x^2` from 0 to 3, the following code can be used:

```
from scipy.integrate import quad

def f(x):
    return x**2

result, error = quad(f, 0, 3)
print(result)
```

This will output `9.0` which is the result of the integration.

## Code explanation

1. `from scipy.integrate import quad` - imports the quad function from the scipy.integrate sub-package
2. `def f(x):` - defines the function to be integrated
3. `result, error = quad(f, 0, 3)` - calls the quad function to integrate the function f from 0 to 3
4. `print(result)` - prints the result of the integration

## Helpful links
- [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html)
- [scipy.integrate.quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html)

onelinerhub: [How can I use Python and SciPy to perform numerical integration?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-perform-numerical-integration)