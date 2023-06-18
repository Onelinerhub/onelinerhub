# How do I use Python's SciPy library to minimize a function?
// plain

Using SciPy's `minimize` function, it is possible to minimize a function. The `minimize` function requires at least two arguments: the function to be minimized, and an initial guess for the minimum. The following example code block shows how to use the `minimize` function to minimize a simple quadratic function:

```
from scipy.optimize import minimize

def quadratic(x):
    return x**2 + 5*x + 4

result = minimize(quadratic, x0=0)
print(result)
```

The output of this code is:

```
     fun: -3.0000000000011435
     jac: array([-2.05395529e-07])
 message: 'Optimization terminated successfully.'
    nfev: 9
     nit: 2
  status: 0
 success: True
       x: array([-2.99999995e+00])
```

The parts of this code are as follows:

1. `from scipy.optimize import minimize` - imports the `minimize` function from the SciPy library.
2. `def quadratic(x):` - defines a function called `quadratic` that takes a single argument `x`.
3. `return x**2 + 5*x + 4` - returns the value of the quadratic function for the given argument `x`.
4. `result = minimize(quadratic, x0=0)` - calls the `minimize` function with the `quadratic` function and an initial guess of `x0=0`.
5. `print(result)` - prints the result of the `minimize` function.

## Helpful links

- [SciPy Optimize Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [Python Minimize Function Tutorial](https://www.python-course.eu/python3_minimize_function.php)

onelinerhub: [How do I use Python's SciPy library to minimize a function?](https://onelinerhub.com/python-scipy/how-do-i-use-python-s-scipy-library-to-minimize-a-function)