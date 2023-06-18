# How can I use Python, SciPy and stats.rvs to generate random variables?
// plain

Python, SciPy and stats.rvs can be used together to generate random variables. To do this, the following steps can be taken:

1. Import the required libraries.
```python
import numpy as np
import scipy.stats as stats
```

2. Generate random variables using stats.rvs.
```python
# Generate a random variable with a normal distribution
normal_dist = stats.rvs(size=1000, loc=0, scale=1)

# Generate a random variable with a uniform distribution
uniform_dist = stats.rvs(size=1000, loc=0, scale=10)
```

3. Use the generated variables to plot a histogram.
```python
import matplotlib.pyplot as plt

# Plot the normal distribution
plt.hist(normal_dist, bins=20, color='c')
plt.axvline(normal_dist.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(normal_dist.mean() + normal_dist.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(normal_dist.mean() - normal_dist.std(), color='b', linestyle='dashed', linewidth=2)
plt.show()

# Plot the uniform distribution
plt.hist(uniform_dist, bins=20, color='c')
plt.axvline(uniform_dist.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(uniform_dist.mean() + uniform_dist.std(), color='b', linestyle='dashed', linewidth=2)
plt.axvline(uniform_dist.mean() - uniform_dist.std(), color='b', linestyle='dashed', linewidth=2)
plt.show()
```

## Helpful links
* [scipy.stats.rvs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rvs.html)
* [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html)

onelinerhub: [How can I use Python, SciPy and stats.rvs to generate random variables?](https://onelinerhub.com/python-scipy/how-can-i-use-python--scipy-and-stats-rvs-to-generate-random-variables)