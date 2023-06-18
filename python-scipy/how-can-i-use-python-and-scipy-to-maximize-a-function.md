# How can I use Python and SciPy to maximize a function?
// plain

To maximize a function with Python and SciPy, you can use the [`scipy.optimize.minimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html) function. This function requires a function to minimize, an initial guess for the parameters, and a method of optimization. For example, you could use the [`SLSQP`](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html) method to maximize the function `f(x,y) = x^2 + y^2` with initial guess `x=1` and `y=1`:

```
import numpy as np
from scipy.optimize import minimize

def f(x):
    x1 = x[0]
    x2 = x[1]
    return x1**2 + x2**2

x0 = np.array([1.0, 1.0])
res = minimize(f, x0, method='SLSQP')

print(res.x)
```

## Output example

```
[0. 0.]
```

The code above consists of the following parts:

1. `import numpy as np`: import the `numpy` library as `np`
2. `from scipy.optimize import minimize`: import the `minimize` function from the `scipy.optimize` library
3. `def f(x):`: define the function `f(x)` to be minimized
4. `x0 = np.array([1.0, 1.0])`: create a `numpy` array with the initial guess for the parameters
5. `res = minimize(f, x0, method='SLSQP')`: call the `minimize` function with the function `f`, the initial guess `x0`, and the optimization method `SLSQP`
6. `print(res.x)`: print the optimized parameters

For more information on using Python and SciPy to maximize a function, see the following links:

- [Scipy Optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [Scipy Optimize Tutorial](https://scipy-lectures.org/advanced/mathematical_optimization/index.html)

onelinerhub: [How can I use Python and SciPy to maximize a function?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-maximize-a-function)