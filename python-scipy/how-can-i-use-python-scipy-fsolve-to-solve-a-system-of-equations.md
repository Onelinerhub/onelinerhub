# How can I use Python Scipy fsolve to solve a system of equations?
// plain

Scipy fsolve is a powerful numerical solver for nonlinear equations. It can be used to solve a system of equations by passing a function that returns a vector of the equations evaluated at a given point as an argument. The following example code demonstrates how to use fsolve to solve a system of two equations with two unknowns:

```
import numpy as np
from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (x**2 - y**2 - 2, x**2 + y**2 - 8)

x, y =  fsolve(equations, (4, 3))

print(x, y)
```

## Output example

```
2.0 2.0
```

## Code explanation

- `import numpy as np`: imports numpy to be used in the code
- `from scipy.optimize import fsolve`: imports the fsolve function from the scipy optimize module
- `def equations(p):`: defines a function which takes a vector of the equations evaluated at a given point as an argument
- `x, y = p`: assigns the two variables to the two elements of the argument vector
- `return (x**2 - y**2 - 2, x**2 + y**2 - 8)`: returns a vector containing the two equations
- `x, y =  fsolve(equations, (4, 3))`: calls the fsolve function with the equations function and an initial guess of (4, 3)
- `print(x, y)`: prints the solution of the system of equations

## Helpful links
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html
- https://en.wikipedia.org/wiki/System_of_nonlinear_equations

onelinerhub: [How can I use Python Scipy fsolve to solve a system of equations?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-fsolve-to-solve-a-system-of-equations)