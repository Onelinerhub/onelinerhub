# How do I fit a Gaussian distribution using Python and SciPy?
// plain

To fit a Gaussian distribution using Python and SciPy, you can use the `scipy.stats.norm.fit()` function. This function takes an array of data samples and returns the mean and standard deviation of the best fitting Gaussian distribution.

## Example code

```
from scipy.stats import norm

# Generate random data
data = np.random.randn(10000)

# Fit a normal distribution to the data
mu, std = norm.fit(data)

print('mu:', mu)
print('std:', std)
```

## Output example

```
mu: 0.007817331827256067
std: 0.9908788996850786
```

The code above does the following:

1. Imports the `norm` function from the `scipy.stats` module.
2. Generates an array of random data using `np.random.randn()`.
3. Fits a normal distribution to the data using `norm.fit()`.
4. Prints the mean and standard deviation of the best fitting Gaussian distribution.

## Helpful links
- [scipy.stats.norm.fit() documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.fit.html)
- [numpy.random.randn() documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html)

onelinerhub: [How do I fit a Gaussian distribution using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-fit-a-gaussian-distribution-using-python-and-scipy)