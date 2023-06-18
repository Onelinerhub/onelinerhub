# How do I use Python Scipy to generate distributions?
// plain

Python Scipy can be used to generate distributions by using the `scipy.stats` module. For example, to generate a normal distribution with mean 0 and standard deviation 1, you can use the following code:

```
from scipy.stats import norm

# Generate random numbers from N(0,1)
data_normal = norm.rvs(size=1000,loc=0,scale=1)
```

The `norm.rvs` function takes the following parameters:

* `size`: The number of random variables to generate
* `loc`: The mean of the distribution
* `scale`: The standard deviation of the distribution

You can also generate other distributions such as binomial, poisson, gamma, and many more. For more information, please refer to the [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.html).

onelinerhub: [How do I use Python Scipy to generate distributions?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-generate-distributions)