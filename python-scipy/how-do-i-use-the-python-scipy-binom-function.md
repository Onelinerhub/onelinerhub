# How do I use the Python Scipy binom function?
// plain

The `scipy.stats.binom` function is a part of the SciPy library and is used to calculate the probability mass function (PMF) or cumulative density function (CDF) of a binomial distribution. A binomial distribution is a statistical distribution used to model the probability of a given number of successes in a set number of independent trials.

## Example code

```
from scipy.stats import binom

# Calculate the probability of getting exactly 3 heads in 10 coin flips
binom.pmf(3, 10, 0.5)
```

## Output example

```
0.11718750000000006
```

The code above calculates the probability mass function (PMF) of a binomial distribution with 10 trials and a probability of success of 0.5. The probability of getting exactly 3 heads in 10 coin flips is 0.11718750000000006.

The `scipy.stats.binom` function can also be used to calculate the cumulative density function (CDF) of a binomial distribution.

## Example code

```
from scipy.stats import binom

# Calculate the probability of getting 3 or fewer heads in 10 coin flips
binom.cdf(3, 10, 0.5)
```

## Output example

```
0.998046875
```

The code above calculates the cumulative density function (CDF) of a binomial distribution with 10 trials and a probability of success of 0.5. The probability of getting 3 or fewer heads in 10 coin flips is 0.998046875.

## Code explanation

- `from scipy.stats import binom`: this imports the `binom` function from the SciPy library.
- `binom.pmf(3, 10, 0.5)`: this calculates the probability mass function (PMF) of a binomial distribution with 10 trials and a probability of success of 0.5, and returns the probability of getting exactly 3 successes.
- `binom.cdf(3, 10, 0.5)`: this calculates the cumulative density function (CDF) of a binomial distribution with 10 trials and a probability of success of 0.5, and returns the probability of getting 3 or fewer successes.

## Helpful links
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html)
- [Wikipedia - Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution)

onelinerhub: [How do I use the Python Scipy binom function?](https://onelinerhub.com/python-scipy/how-do-i-use-the-python-scipy-binom-function)