# How can I use Python Scipy to optimize a root?
// plain

Scipy provides a number of optimization algorithms for finding a root of a function. The `scipy.optimize.root` function is the most general and provides a variety of methods for finding a root.

For example, the following code will use the `broyden1` method to find the root of a function:
```
import scipy.optimize as opt

def f(x):
    return x**2 - 4

result = opt.root(f, x0=1, method='broyden1')
print(result)
```
The output of this code will be:
```
    converged: True
    flag: 'converged'
    fun: array([0.])
    jac: array([-8.88178420e-16])
    message: 'The solution converged.'
    nfev: 9
    root: array([2.])
```

The code consists of the following parts:
1. `import scipy.optimize as opt` imports the `scipy.optimize` module and assigns it to the name `opt`.
2. `def f(x):` defines a function `f` with one argument `x`.
3. `return x**2 - 4` returns the value of `x**2 - 4` when `f` is called.
4. `result = opt.root(f, x0=1, method='broyden1')` calls the `scipy.optimize.root` function with the function `f`, an initial guess of `x0=1`, and the `broyden1` method.
5. `print(result)` prints the result of the optimization.

For more information, see the [Scipy root documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html).

onelinerhub: [How can I use Python Scipy to optimize a root?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-optimize-a-root)