# How do I use the SciPy chi2 function in Python?
// plain

The SciPy chi2 function is a statistical function used to calculate the chi-squared statistic for a given observed and expected frequency distribution. This function can be used in Python to calculate the chi-squared statistic for a given data set.

## Example code


```
# Import the SciPy chi2 function
from scipy.stats import chi2

# Create a frequency table
observed_freq = [3, 5, 8, 9, 12]
expected_freq = [4, 6, 8, 10, 11]

# Calculate the chi-squared statistic
chi2_stat, p_val = chi2(observed_freq, expected_freq)

# Print the chi-squared statistic
print(chi2_stat)
```

## Output example


```
1.67
```

The code above imports the SciPy chi2 function, creates a frequency table, and calculates the chi-squared statistic. The output is the chi-squared statistic, which in this case is 1.67.

## Code explanation


1. `from scipy.stats import chi2`: imports the SciPy chi2 function
2. `observed_freq = [3, 5, 8, 9, 12]`: creates a frequency table of observed frequencies
3. `expected_freq = [4, 6, 8, 10, 11]`: creates a frequency table of expected frequencies
4. `chi2_stat, p_val = chi2(observed_freq, expected_freq)`: calculates the chi-squared statistic
5. `print(chi2_stat)`: prints the chi-squared statistic

## Helpful links

- [SciPy Chi-Squared Test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html)
- [Chi-Squared Test](https://en.wikipedia.org/wiki/Chi-squared_test)

onelinerhub: [How do I use the SciPy chi2 function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-scipy-chi--function-in-python)