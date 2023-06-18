# How can I use Python SciPy to minimize a function with constraints?
// plain

The Python SciPy library provides a variety of optimization functions, including the ability to minimize a function with constraints. To do this, one can use the scipy.optimize.minimize function with the method argument set to 'SLSQP'. This algorithm uses a quasi-Newton method to minimize a function with constraints.

The following example shows how to use the scipy.optimize.minimize function to minimize a simple function with two constraints.

```
import scipy.optimize as opt

# Define objective function
def objective(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

# Define constraint 1
def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0

# Define constraint 2
def constraint2(x):
    sum_eq = 40.0
    for i in range(4):
        sum_eq = sum_eq - x[i]**2
    return sum_eq

# Initial guesses
x0 = [1,5,5,1]

# Show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# Call the optimize function
b = (1.0,5.0)
bnds = (b, b, b, b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = ([con1,con2])
solution = opt.minimize(objective,x0,method='SLSQP',\
                        bounds=bnds,constraints=cons)
x = solution.x

# Show final objective
print('Final SSE Objective: ' + str(objective(x)))

# Print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
print('x4 = ' + str(x[3]))
```

## Output example

```
Initial SSE Objective: 16
Final SSE Objective: 17.01401724563517
Solution
x1 = 1.0
x2 = 4.7430034
x3 = 3.8211536
x4 = 1.3794074
```

## Code explanation

- `import scipy.optimize as opt`: imports the SciPy optimization library.
- `def objective(x):`: defines the objective function to be minimized.
- `def constraint1(x):` and `def constraint2(x):`: define the constraints on the objective function.
- `x0 = [1,5,5,1]`: sets the initial guesses for the variables.
- `b = (1.0,5.0)` and `bnds = (b, b, b, b)`: sets the bounds on the variables.
- `con1 = {'type': 'ineq', 'fun': constraint1}` and `con2 = {'type': 'eq', 'fun': constraint2}`: defines the constraint types (inequality or equality).
- `cons = ([con1,con2])`: combines the constraints into a single list.
- `solution = opt.minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)`: calls the scipy.optimize.minimize function to minimize the objective function with the constraints.
- `x = solution.x`: stores the solution in an array.
- `print('Solution')` and `print('x1 = ' + str(x[0]))`: prints the solution.

## Helpful links
- [SciPy Optimize Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [SciPy SLSQP Algorithm Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize)

onelinerhub: [How can I use Python SciPy to minimize a function with constraints?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-minimize-a-function-with-constraints)