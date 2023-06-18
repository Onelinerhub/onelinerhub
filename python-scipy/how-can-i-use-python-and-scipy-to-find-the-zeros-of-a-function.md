# How can I use Python and SciPy to find the zeros of a function?
// plain

Using Python and SciPy to find the zeros of a function can be done with the `scipy.optimize.fsolve` function. This function takes a function, and an initial guess, and returns the zero of the function.

For example, to find the zero of the function `f(x) = x^2 + 2x - 3`, we can use the following code:

```
from scipy.optimize import fsolve

def f(x):
    return x**2 + 2*x - 3

x_zero = fsolve(f, 0)
print(x_zero)
```

## Output example

```
[-3.]
```

The code consists of the following parts:

1. Importing the `scipy.optimize.fsolve` function from the SciPy library: `from scipy.optimize import fsolve`
2. Defining the function to find the zero of: `def f(x): return x**2 + 2*x - 3`
3. Calling the `fsolve` function with the function and initial guess as arguments: `x_zero = fsolve(f, 0)`
4. Printing the zero of the function: `print(x_zero)`

## Helpful links
- [scipy.optimize.fsolve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html)
- [Python Tutorial](https://www.tutorialspoint.com/python/index.htm)

onelinerhub: [How can I use Python and SciPy to find the zeros of a function?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-find-the-zeros-of-a-function)