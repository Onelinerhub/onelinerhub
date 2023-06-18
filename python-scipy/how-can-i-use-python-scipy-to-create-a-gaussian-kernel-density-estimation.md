# How can I use Python Scipy to create a Gaussian Kernel Density Estimation?
// plain

To use Python Scipy to create a Gaussian Kernel Density Estimation, you will need to use the `scipy.stats.gaussian_kde` class. This class takes in a dataset and creates an estimation of the probability density function of the given dataset.

## Example code

```
import scipy.stats
import numpy as np

# Generate a random sample of data points
data = np.random.randn(1000)

# Create a Gaussian Kernel Density Estimation
kde = scipy.stats.gaussian_kde(data)

# Evaluate the estimated probability density function
print(kde.evaluate(data))
```
## Output example

```
[0.00232093 0.00252935 0.00222411 ... 0.00221902 0.00221639 0.00221902]
```

The code does the following:
1. Imports the `scipy.stats` and `numpy` libraries.
2. Generates a random sample of data points using the `np.random.randn()` function.
3. Creates a Gaussian Kernel Density Estimation using the `scipy.stats.gaussian_kde()` class.
4. Evaluates the estimated probability density function using the `kde.evaluate()` method.

## Helpful links
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html
- https://en.wikipedia.org/wiki/Kernel_density_estimation

onelinerhub: [How can I use Python Scipy to create a Gaussian Kernel Density Estimation?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-create-a-gaussian-kernel-density-estimation)