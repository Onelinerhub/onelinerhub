# How do I use Python Scipy to perform a linear fit?
// plain

Using Scipy to perform a linear fit is quite easy. First, import the `scipy.optimize` module which contains the `curve_fit` function:

```python
from scipy.optimize import curve_fit
```

Then, define a function that describes the linear model:

```python
def linear_model(x, a, b):
    return a * x + b
```

Next, define the data points to fit:

```python
x_data = [0, 1, 2, 3]
y_data = [1, 3, 5, 7]
```

Finally, use the `curve_fit` function to fit the linear model to the data:

```python
params, params_covariance = curve_fit(linear_model, x_data, y_data)
```

The `params` variable contains the two parameters of the linear model, `a` and `b`, which are the slope and intercept respectively. For example, the output of the above code is:

```
params = [2. 1.]
```

This means that the linear model is `y = 2x + 1`.

## Code explanation
**
1. `from scipy.optimize import curve_fit` - imports the `curve_fit` function from the `scipy.optimize` module
2. `def linear_model(x, a, b):` - defines a function that describes the linear model
3. `x_data = [0, 1, 2, 3]` - defines the x-values of the data points
4. `y_data = [1, 3, 5, 7]` - defines the y-values of the data points
5. `params, params_covariance = curve_fit(linear_model, x_data, y_data)` - uses the `curve_fit` function to fit the linear model to the data

**## Helpful links**
- [Scipy Optimize Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [Python Curve Fitting Tutorial](https://realpython.com/linear-regression-in-python/)

onelinerhub: [How do I use Python Scipy to perform a linear fit?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-perform-a-linear-fit)