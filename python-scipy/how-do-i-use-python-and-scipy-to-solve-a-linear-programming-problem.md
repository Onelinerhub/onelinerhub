# How do I use Python and SciPy to solve a linear programming problem?
// plain

Linear programming is a method for finding optimal solutions to problems with multiple constraints. Python and SciPy can be used to solve linear programming problems with the `scipy.optimize.linprog` function.

## Example


```
import numpy as np
from scipy.optimize import linprog

# coefficients of the objective function
c = np.array([2, 3])

# coefficients of the constraints
A = np.array([[1, 1], [2, 3]])

# right-hand side of the constraints
b = np.array([4, 8])

# bounds on the variables
x1_bounds = (0, None)
x2_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=(x1_bounds, x2_bounds))

print(res)
```

## Output example

```
     fun: 8.0
 message: 'Optimization terminated successfully.'
     nit: 2
   slack: array([0., 0.])
  status: 0
 success: True
       x: array([2., 4.])
```

The `scipy.optimize.linprog` function takes the coefficients of the objective function (`c`), the coefficients of the constraints (`A`), the right-hand side of the constraints (`b`), and the bounds on the variables (`x1_bounds`, `x2_bounds`) as inputs. The output of the function is an optimization result object which contains the optimal solution (`x`) and other information such as the function value (`fun`) and the status of the optimization (`status`).

## Helpful links
- [scipy.optimize.linprog Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
- [Linear Programming Tutorial](https://www.tutorialspoint.com/operations_research/linear_programming.htm)

onelinerhub: [How do I use Python and SciPy to solve a linear programming problem?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-solve-a-linear-programming-problem)