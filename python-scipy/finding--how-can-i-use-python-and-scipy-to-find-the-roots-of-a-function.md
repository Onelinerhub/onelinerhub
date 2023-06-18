# finding

How can I use Python and SciPy to find the roots of a function?
// plain

Python and SciPy can be used to find the roots of a function. To do this, the `scipy.optimize.root` function can be used. This function is part of the SciPy library and requires that the function for which the roots are being found is in the form of a function object. The function takes a number of parameters, including the function, the initial guess for the root, and an optional method.

## Example code

```
from scipy.optimize import root

def f(x):
    return x**2 + 2*x + 1

result = root(f, 0)

print(result.x)
```
## Output example

```
[-1.]
```

## Code explanation

- `from scipy.optimize import root` - imports the `root` function from the SciPy library
- `def f(x):` - defines a function for which the root is being found
- `return x**2 + 2*x + 1` - the function being used to find the root
- `result = root(f, 0)` - calls the `root` function with the function `f` and an initial guess of `0`
- `print(result.x)` - prints the result of the `root` function

## Helpful links
- [SciPy Optimize Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [SciPy Root Finding Tutorial](https://scipy-lectures.org/advanced/mathematical_optimization/index.html#root-finding)

onelinerhub: [finding

How can I use Python and SciPy to find the roots of a function?](https://onelinerhub.com/python-scipy/finding--how-can-i-use-python-and-scipy-to-find-the-roots-of-a-function)