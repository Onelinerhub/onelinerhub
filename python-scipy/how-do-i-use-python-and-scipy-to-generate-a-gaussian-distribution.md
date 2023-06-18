# How do I use Python and SciPy to generate a Gaussian distribution?
// plain

The SciPy library provides a number of functions for generating a Gaussian distribution. To use Python and SciPy to generate a Gaussian distribution, the following steps need to be taken:

1. Import the SciPy library:
```
import scipy.stats as stats
```

2. Generate the Gaussian distribution using the `stats.norm()` function. The function takes three parameters: mean, standard deviation and size. For example, to generate a Gaussian distribution with mean 0 and standard deviation 1, use:
```
x = stats.norm(0, 1).rvs(1000)
```

3. Plot the Gaussian distribution using the `matplotlib` library.
```
import matplotlib.pyplot as plt

plt.hist(x, bins=30, density=True)
plt.show()
```

The output will be a histogram of the generated Gaussian distribution:

![Gaussian Distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/400px-Normal_Distribution_PDF.svg.png)

## Helpful links

- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/index.html)
- [Matplotlib Documentation](https://matplotlib.org/3.2.1/contents.html)

onelinerhub: [How do I use Python and SciPy to generate a Gaussian distribution?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-generate-a-gaussian-distribution)