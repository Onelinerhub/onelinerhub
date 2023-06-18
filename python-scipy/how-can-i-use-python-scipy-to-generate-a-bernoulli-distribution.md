# How can I use Python Scipy to generate a Bernoulli distribution?
// plain

Using the Python Scipy library, you can generate a Bernoulli distribution by using the `scipy.stats.bernoulli` function. This function takes two parameters, the probability of success and size. The probability of success is the probability of a trial resulting in a success, and size is the number of trials.

```
import scipy.stats as stats

# Generate a Bernoulli distribution with p=0.3
bernoulli_dist = stats.bernoulli(0.3, size=100)

# Print the first 10 values of the distribution
print(bernoulli_dist.rvs(10))

# Output
array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
```

The code above will generate a Bernoulli distribution with a probability of success `p=0.3` and a size of `100` trials. The `stats.bernoulli` function will return a frozen Bernoulli distribution object, which can then be used to generate random numbers with the `rvs` method. In this example, the `rvs` method is used to print the first 10 values of the distribution.

The parts of the code are as follows:
- `import scipy.stats as stats` imports the Scipy stats module.
- `stats.bernoulli(0.3, size=100)` creates a Bernoulli distribution with a probability of success `p=0.3` and a size of `100` trials.
- `bernoulli_dist.rvs(10)` generates 10 random numbers from the Bernoulli distribution.

## Helpful links
- [Scipy Stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Bernoulli Distribution on Wikipedia](https://en.wikipedia.org/wiki/Bernoulli_distribution)

onelinerhub: [How can I use Python Scipy to generate a Bernoulli distribution?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-generate-a-bernoulli-distribution)