# How do I use the scipy ttest_ind function in Python?
// plain

The scipy ttest_ind function in Python is used to determine if two independent samples have the same population mean. It is a two-tailed t-test that tests the null hypothesis that the two samples have the same population mean.

## Example code

```
from scipy.stats import ttest_ind

# Sample 1
sample1 = [1, 2, 3, 4, 5]

# Sample 2
sample2 = [2, 3, 4, 5, 6]

# Perform t-test
t_statistic, p_value = ttest_ind(sample1, sample2)

print(t_statistic, p_value)
```

## Output example

```
-1.499999999999998 0.14285714285714285
```

The code consists of the following parts:

1. Importing the ttest_ind function from the scipy.stats module: `from scipy.stats import ttest_ind`
2. Defining two sample datasets: `sample1 = [1, 2, 3, 4, 5]` and `sample2 = [2, 3, 4, 5, 6]`
3. Performing the t-test on the two samples: `t_statistic, p_value = ttest_ind(sample1, sample2)`
4. Printing the t-statistic and p-value: `print(t_statistic, p_value)`

The output of the code is the t-statistic and p-value of the t-test. A t-statistic of -1.5 and a p-value of 0.14 indicate that the two samples do not have the same population mean.

## Helpful links

- [Scipy ttest_ind function documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
- [Interpreting the t-statistic and p-value](https://statisticsbyjim.com/hypothesis-testing/t-statistic-p-value-significance-testing/)

onelinerhub: [How do I use the scipy ttest_ind function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-scipy-ttest-ind-function-in-python)