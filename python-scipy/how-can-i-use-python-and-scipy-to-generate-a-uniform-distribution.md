# How can I use Python and SciPy to generate a uniform distribution?
// plain

To generate a uniform distribution using Python and SciPy, you can use the `scipy.stats.uniform` module. This module provides a `uniform` class that takes two parameters: `loc` and `scale`. `loc` is the lower bound of the distribution, and `scale` is the difference between the upper and lower bounds.

For example, the following code will generate a uniform distribution between 0 and 10:

```
import scipy.stats as stats

uniform_dist = stats.uniform(loc=0, scale=10)
```

You can then generate random numbers from this distribution using the `rvs` function:

```
random_numbers = uniform_dist.rvs(size=10)

print(random_numbers)
# [9.89569399 7.01456662 8.98391771 8.91355863 3.97722255 5.07906918
#  7.68154078 6.25356775 0.66108565 5.56420246]
```

## Code explanation

- `scipy.stats.uniform`: module containing the `uniform` class
- `uniform`: class used to generate a uniform distribution
- `loc`: lower bound of the distribution
- `scale`: difference between the upper and lower bounds
- `rvs`: function used to generate random numbers from the distribution

## Helpful links
- [scipy.stats.uniform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html)

onelinerhub: [How can I use Python and SciPy to generate a uniform distribution?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-generate-a-uniform-distribution)