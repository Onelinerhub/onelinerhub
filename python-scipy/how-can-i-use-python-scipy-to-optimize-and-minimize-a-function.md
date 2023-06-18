# How can I use Python Scipy to optimize and minimize a function?
// plain

Scipy provides a set of powerful tools for optimization and minimization of functions. The scipy.optimize module contains a variety of optimization algorithms and minimization techniques.

For example, the minimize() function can be used to minimize a given function. The following code block shows an example of using the minimize() function to minimize a simple function:

```
from scipy.optimize import minimize

def objective(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

x0 = [0, 0]
res = minimize(objective, x0)

print(res.x)
```

## Output example

```
[1. 2.5]
```

The code above is composed of the following parts:

1. Import the minimize() function from the scipy.optimize module:
```from scipy.optimize import minimize```

2. Define a function to be minimized:
```def objective(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2
```

3. Set the initial guess of the solution:
```x0 = [0, 0]```

4. Call the minimize() function to find the optimal solution:
```res = minimize(objective, x0)```

5. Print the optimal solution:
```print(res.x)```

For more information, see the following links:

- [Scipy Optimize Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [Minimize Function Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html)

onelinerhub: [How can I use Python Scipy to optimize and minimize a function?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-optimize-and-minimize-a-function)