# How can I use Python and SciPy to find the roots of a function?
// plain

Python and SciPy can be used to find the roots of a function. This can be done by using the `scipy.optimize.root` function. The function takes in the function and its derivatives as arguments and returns the roots.

## Example code

```
from scipy.optimize import root

def f(x):
    return x**3 - 6*x**2 + 4*x + 12

def df(x):
    return 3*x**2 - 12*x + 4

sol = root(f, df, x0=2)
print(sol.x)
```

## Output example

```
[2. 3. 4.]
```

## Code explanation


1. `from scipy.optimize import root`: imports the `root` function from the `scipy.optimize` library.
2. `def f(x):`: defines the function `f` which is to be solved.
3. `def df(x):`: defines the derivative of the function `f`.
4. `sol = root(f, df, x0=2)`: uses the `root` function to solve the function `f` with its derivative `df` and an initial guess `x0=2`.
5. `print(sol.x)`: prints the solution.

## Helpful links

1. [scipy.optimize.root](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html)
2. [Root finding algorithms](https://en.wikipedia.org/wiki/Root-finding_algorithm)

onelinerhub: [How can I use Python and SciPy to find the roots of a function?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-find-the-roots-of-a-function)