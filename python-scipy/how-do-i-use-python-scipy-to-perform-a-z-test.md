# How do I use Python Scipy to perform a Z test?
// plain

`Scipy` is a library for scientific computing in Python. It provides functions for performing various statistical tests, including the Z-test.

To use `Scipy` to perform a Z-test, you will need to import the `stats` module. This module contains the `ztest` function which can be used to perform the Z-test.

```python
from scipy import stats

z_score, p_value = stats.ztest(x1, x2)
```

The `ztest` function takes two arguments, `x1` and `x2` which are the two samples being compared. It returns two values, the `z_score` and the `p_value`. The `z_score` is the standardized test statistic and the `p_value` is the probability of obtaining the observed results, given that the null hypothesis is true.

## Code explanation


1. `from scipy import stats` - imports the `stats` module from the `Scipy` library.
2. `z_score, p_value = stats.ztest(x1, x2)` - calls the `ztest` function from the `stats` module, passing in two samples `x1` and `x2` as arguments. It returns two values, `z_score` and `p_value`.

## Helpful links

- [Scipy Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Z-test Tutorial](https://machinelearningmastery.com/z-test-statistical-significance-testing/)

onelinerhub: [How do I use Python Scipy to perform a Z test?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-perform-a-z-test)