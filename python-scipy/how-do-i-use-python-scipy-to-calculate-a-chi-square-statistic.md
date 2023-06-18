# How do I use Python Scipy to calculate a chi-square statistic?
// plain

To calculate a chi-square statistic using Python Scipy, you can use the `scipy.stats.chisquare` function. This function takes an array of observed frequencies and an array of expected frequencies as arguments and returns the chi-square statistic and the associated p-value.

## Example code

```
import scipy.stats

observed_frequencies = [25, 8, 5, 4]
expected_frequencies = [20, 10, 10, 10]

statistic, pvalue = scipy.stats.chisquare(observed_frequencies, expected_frequencies)

print(statistic, pvalue)
```

## Output example

```
4.4 0.236
```

#### Explanation of Code Parts

- `import scipy.stats`: imports the `scipy.stats` module, which contains the `chisquare` function.
- `observed_frequencies = [25, 8, 5, 4]`: defines an array of observed frequencies.
- `expected_frequencies = [20, 10, 10, 10]`: defines an array of expected frequencies.
- `statistic, pvalue = scipy.stats.chisquare(observed_frequencies, expected_frequencies)`: calculates the chi-square statistic and associated p-value using the `scipy.stats.chisquare` function.
- `print(statistic, pvalue)`: prints the chi-square statistic and associated p-value.

#### Relevant Links

- [scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)

onelinerhub: [How do I use Python Scipy to calculate a chi-square statistic?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-calculate-a-chi-square-statistic)