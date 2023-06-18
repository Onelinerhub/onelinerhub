# How do I calculate the median using Python and SciPy?
// plain

The median is the middle value in a dataset when the values are ordered from smallest to largest. It can be calculated using Python and SciPy with the following steps:

1. Import the SciPy library:
```
import scipy
```

2. Create a list of values in the dataset:
```
data_set = [2, 4, 6, 8, 10, 12, 14]
```

3. Calculate the median using the median() function:
```
median = scipy.median(data_set)
print(median)
```
## Output example

```
8
```

4. The median of the dataset is 8.

## Helpful links

- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.median.html)
- [Python for Data Science: Calculating the Median](https://www.dataquest.io/blog/numpy-tutorial-python/)

onelinerhub: [How do I calculate the median using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-calculate-the-median-using-python-and-scipy)