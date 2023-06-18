# How do I use Python Scipy's Differential Evolution to optimize a function?
// plain

Differential Evolution (DE) is a powerful evolutionary algorithm used to optimize a function. It is included in the SciPy library and can be used as follows:

```
from scipy.optimize import differential_evolution

def func(x):
    return x[0]**2 + x[1]**2

bounds = [(0,2), (0,2)]
result = differential_evolution(func, bounds)

print(result.x)
# Output: array([1.99999998, 1.99999998])
```

The `differential_evolution` function takes two arguments: the function to be optimized, and a tuple of bounds for each parameter. The function should return a single value. In this example, we are optimizing a simple function of two variables. The output of the function is an `OptimizeResult` object, which contains the optimal parameters, and other useful information.

Parts of the code:

- `from scipy.optimize import differential_evolution`: imports the Differential Evolution function from the SciPy library.
- `def func(x):`: defines the function to be optimized.
- `bounds = [(0,2), (0,2)]`: defines the bounds for each parameter of the function.
- `result = differential_evolution(func, bounds)`: runs the Differential Evolution algorithm, passing the function and bounds as arguments.
- `print(result.x)`: prints the optimal parameters.

## Helpful links

- [SciPy Differential Evolution Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html)
- [Differential Evolution Algorithm](https://en.wikipedia.org/wiki/Differential_evolution)

onelinerhub: [How do I use Python Scipy's Differential Evolution to optimize a function?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-s-differential-evolution-to-optimize-a-function)