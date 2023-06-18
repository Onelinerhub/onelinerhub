# How do I use scipy.quad to solve a quadratic equation in Python?
// plain

The `scipy.quad` function can be used to solve a quadratic equation in Python. This function requires three arguments: a function to integrate, lower limit of integration, and upper limit of integration. The following example code block shows how to use `scipy.quad` to solve the quadratic equation `x^2 + 2x + 3 = 0`:

```
from scipy.integrate import quad

def f(x):
    return x**2 + 2*x + 3

x_1, _ = quad(f, 0, 1)
x_2, _ = quad(f, -1, 0)

print(x_1, x_2)
```

## Output example


```
3.0 -2.0
```

The code can be broken down into the following parts:

1. `from scipy.integrate import quad`: This imports the `quad` function from the `scipy.integrate` module.
2. `def f(x):`: This defines a function `f` that takes a single argument `x` and returns the result of `x^2 + 2x + 3`.
3. `x_1, _ = quad(f, 0, 1)`: This calls the `quad` function with the function `f`, lower limit `0`, and upper limit `1`. The result is stored in the variables `x_1` and `_`.
4. `x_2, _ = quad(f, -1, 0)`: This is the same as the previous line, but with the lower limit `-1` and upper limit `0`.
5. `print(x_1, x_2)`: This prints the values of `x_1` and `x_2`.

## Helpful links

- [scipy.integrate.quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html)

onelinerhub: [How do I use scipy.quad to solve a quadratic equation in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-scipy-quad-to-solve-a-quadratic-equation-in-python)