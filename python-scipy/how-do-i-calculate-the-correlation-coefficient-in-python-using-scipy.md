# How do I calculate the correlation coefficient in Python using SciPy?
// plain

The correlation coefficient can be calculated in Python using SciPy's `pearsonr` function. This function takes two arrays of equal length and returns the Pearson correlation coefficient and the p-value for testing non-correlation. The Pearson correlation coefficient is a measure of the linear correlation between two variables.

## Example code

```
from scipy.stats import pearsonr
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
corr, p_value = pearsonr(x, y)
print(corr)
```

## Output example

```
1.0
```

The code consists of four parts:
1. Importing the Pearson correlation coefficient function from the SciPy package.
2. Defining two arrays of equal length.
3. Calculating the Pearson correlation coefficient and the p-value for testing non-correlation by calling the `pearsonr` function with the two arrays as arguments.
4. Printing the Pearson correlation coefficient.

## Helpful links
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
- https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/

onelinerhub: [How do I calculate the correlation coefficient in Python using SciPy?](https://onelinerhub.com/python-scipy/how-do-i-calculate-the-correlation-coefficient-in-python-using-scipy)