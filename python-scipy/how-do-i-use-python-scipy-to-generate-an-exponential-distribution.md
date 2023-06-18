# How do I use Python Scipy to generate an exponential distribution?
// plain

Scipy is a powerful python library for scientific computing. It provides a wide range of functions for generating and manipulating probability distributions. To generate an exponential distribution using Scipy, the `scipy.stats.expon` function can be used.

## Example code

```
import scipy.stats

x = scipy.stats.expon.rvs(size=10)
print(x)
```

Example output:
```
[1.97790379 0.96668961 0.37204524 0.18509819 0.14698962 1.78867799
 0.73548481 0.30222099 0.73564717 0.61254917]
```

## Code explanation

* `import scipy.stats`: imports the `scipy.stats` module
* `scipy.stats.expon.rvs(size=10)`: generates 10 random variables from an exponential distribution
* `print(x)`: prints the generated random variables

## Helpful links
* [Scipy Documentation](https://docs.scipy.org/doc/scipy/reference/)
* [Exponential Distribution in Scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html)

onelinerhub: [How do I use Python Scipy to generate an exponential distribution?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-generate-an-exponential-distribution)