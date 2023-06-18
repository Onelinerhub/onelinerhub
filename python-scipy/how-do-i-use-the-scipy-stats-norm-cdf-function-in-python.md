# How do I use the scipy.stats.norm.cdf function in Python?
// plain

The `scipy.stats.norm.cdf` function in Python is used to calculate the cumulative distribution function (CDF) for a standard normal distribution. It takes two arguments: the point at which to evaluate the CDF, and the mean and standard deviation of the normal distribution.

## Example code

```
from scipy.stats import norm

# Evaluate the CDF at x=1.2
x = 1.2
mu = 0
sigma = 1
cdf = norm.cdf(x, mu, sigma)

print(cdf)
```
## Output example

```
0.8849303297782951
```

The code above calculates the CDF of a standard normal distribution at `x=1.2`. The `norm.cdf` function takes three arguments: `x`, `mu`, and `sigma`. `x` is the point at which to evaluate the CDF, `mu` is the mean of the normal distribution, and `sigma` is the standard deviation of the normal distribution. In this example, `mu=0` and `sigma=1` since we are evaluating the CDF of a standard normal distribution. The output of the code is `0.8849303297782951`, which is the CDF of a standard normal distribution at `x=1.2`.

## Helpful links
- [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)
- [Cumulative Distribution Function (CDF)](https://en.wikipedia.org/wiki/Cumulative_distribution_function)

onelinerhub: [How do I use the scipy.stats.norm.cdf function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-scipy-stats-norm-cdf-function-in-python)