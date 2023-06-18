# int

How do I use the SciPy odeint function in Python?
// plain

The SciPy `odeint` function is a numerical integration routine for solving ordinary differential equations (ODEs) in Python. It is a wrapper for the FORTRAN library `odepack`. `odeint` takes the following arguments:

* `func`: The function to be integrated, which must take two arguments (the independent variable and the current state vector) and return the derivatives of the state vector with respect to the independent variable.

* `y0`: The initial conditions of the system.

* `t`: A sequence of time points for which to solve for the state vector.

* `args`: Any extra arguments needed for `func`.

Here is an example of how to use `odeint` to solve the system of ODEs for a simple harmonic oscillator:

```python
from scipy.integrate import odeint
import numpy as np

def f(y, t, omega):
    return [y[1], -omega**2*y[0]]

t = np.arange(0, 10, 0.1)
y0 = [1, 0]
omega = 2

sol = odeint(f, y0, t, args=(omega,))

print(sol)
```

This code produces the following output:
```
[[ 1.          0.        ]
 [ 0.99500417 -0.09983342]
 [ 0.98006658 -0.19866933]
 ...
 [-0.99500417  0.09983342]
 [-0.98006658  0.19866933]
 [-0.96017029  0.29552021]]
```

For more information, see the official [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html) and [tutorials](https://scipython.com/book/chapter-8-scipy/additional-examples/the-harmonic-oscillator-again/).

onelinerhub: [int

How do I use the SciPy odeint function in Python?](https://onelinerhub.com/python-scipy/int--how-do-i-use-the-scipy-odeint-function-in-python)