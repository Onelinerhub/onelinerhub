# How can I use Python Scipy's random variate sampling functions?
// plain

Scipy's random variate sampling functions allow you to generate random numbers from a variety of probability distributions. You can use the `scipy.stats.rvs()` function to generate random variates from a given probability distribution. For example, to generate random variates from a standard normal distribution, you can use the following code:

```
from scipy.stats import norm

# Generate 10 random variates from a standard normal distribution
norm.rvs(size=10)

# Output: array([-0.81418096,  1.56905525, -0.46947439,  0.35678637,  1.06354542,
#                 0.32738587, -0.91928847, -0.84538123,  0.67752869, -1.05862925])
```

The code above consists of the following parts:

1. `from scipy.stats import norm`: This imports the `norm` class from the `scipy.stats` module, which contains functions related to the normal probability distribution.

2. `norm.rvs(size=10)`: This calls the `norm.rvs()` function, which generates random variates from a standard normal distribution. The `size` argument specifies the number of random variates to generate.

More information about Scipy's random variate sampling functions can be found in the [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/stats.html#random-variate-sampling).

onelinerhub: [How can I use Python Scipy's random variate sampling functions?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-s-random-variate-sampling-functions)