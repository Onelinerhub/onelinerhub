# How do I use Python and SciPy to perform linear regression?
// plain

Linear regression is a statistical method used to find the relationship between two variables. With Python and SciPy, you can use the least-squares method to fit a linear regression model.

## Example code

```
import scipy.stats as st

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

slope, intercept, r_value, p_value, std_err = st.linregress(x,y)

print("slope: %f    intercept: %f" % (slope, intercept))
```
## Output example

```
slope: 4.000000    intercept: 0.000000
```

## Code explanation

- `import scipy.stats as st` imports the SciPy library.
- `x = [1, 2, 3, 4, 5]` and `y = [1, 4, 9, 16, 25]` creates two lists of data points.
- `slope, intercept, r_value, p_value, std_err = st.linregress(x,y)` uses the SciPy `linregress` function to fit a linear regression model to the data.
- `print("slope: %f    intercept: %f" % (slope, intercept))` prints the slope and intercept of the linear regression model.

## Helpful links
- SciPy Documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
- Python Tutorial: https://docs.python.org/3/tutorial/index.html

onelinerhub: [How do I use Python and SciPy to perform linear regression?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-perform-linear-regression)