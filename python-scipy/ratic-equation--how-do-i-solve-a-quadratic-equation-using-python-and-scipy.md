# ratic equation

How do I solve a quadratic equation using Python and SciPy?
// plain

A quadratic equation is an equation of the form `ax^2 + bx + c = 0`. It can be solved using Python and SciPy by using the `scipy.optimize.root()` function. This function takes three parameters: a function, an initial guess, and a method. The function is the equation itself, the initial guess is an initial value for the solution, and the method is the type of solver used.

For example, to solve the equation `x^2 + 2x + 1 = 0`, the following code can be used:

```python
import scipy.optimize

def f(x):
    return x**2 + 2*x + 1

sol = scipy.optimize.root(f, 0.5, method='broyden1')
print(sol.x)
```

This code will output `[-1.]`, which is the solution to the equation.

The code consists of the following parts:

* `import scipy.optimize`: This imports the SciPy package, which contains the `root()` function.
* `def f(x):`: This defines the function `f`, which is the equation itself.
* `sol = scipy.optimize.root(f, 0.5, method='broyden1')`: This uses the `root()` function to solve the equation. The parameters passed to the function are the equation (`f`), the initial guess (`0.5`), and the method (`broyden1`).
* `print(sol.x)`: This prints the solution to the equation.

## Helpful links

* [SciPy Optimize Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
* [SciPy Root Finding Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html)

onelinerhub: [ratic equation

How do I solve a quadratic equation using Python and SciPy?](https://onelinerhub.com/python-scipy/ratic-equation--how-do-i-solve-a-quadratic-equation-using-python-and-scipy)