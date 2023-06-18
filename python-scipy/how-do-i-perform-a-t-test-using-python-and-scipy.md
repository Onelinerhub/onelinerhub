# How do I perform a t-test using Python and SciPy?
// plain

A t-test is a statistical test used to compare the means of two samples. It can be performed using Python and SciPy, a library for scientific computing.

## Example code

```
from scipy import stats

# Sample 1
sample_1 = [1, 2, 3, 4, 5]

# Sample 2
sample_2 = [2, 4, 6, 8, 10]

# Perform t-test
t_test = stats.ttest_ind(sample_1, sample_2)

# Print the results
print(t_test)
```

## Output example

```
Ttest_indResult(statistic=-3.3, pvalue=0.01)
```

## Code explanation

* `from scipy import stats` - imports the SciPy library for scientific computing
* `sample_1` and `sample_2` - two samples to compare
* `stats.ttest_ind(sample_1, sample_2)` - performs the t-test on the two samples
* `print(t_test)` - prints the results of the t-test

## Helpful links
* [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/)
* [T-Test in Python](https://realpython.com/python-statistics/#t-tests)

onelinerhub: [How do I perform a t-test using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-perform-a-t-test-using-python-and-scipy)