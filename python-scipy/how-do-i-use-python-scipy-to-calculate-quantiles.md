# How do I use Python Scipy to calculate quantiles?
// plain

Scipy is a powerful Python library for scientific computing. It includes a module for calculating quantiles, scipy.stats.mstats.mquantiles. The mquantiles function takes in an array of values and a set of quantiles and returns an array of the same size as the quantiles given with the values in the input array that correspond to the given quantiles.

## Example code

```
import scipy.stats

# Create an array of values
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the quantiles for the array
quantiles = scipy.stats.mstats.mquantiles(values, [0.25, 0.5, 0.75])

# Print the results
print(quantiles)
```

## Output example

```
[3. 5. 7.]
```

## Code explanation

- `import scipy.stats`: imports the scipy module for scientific computing
- `values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`: creates an array of 10 values
- `scipy.stats.mstats.mquantiles(values, [0.25, 0.5, 0.75])`: calculates the quantiles for the given array and quantile values
- `print(quantiles)`: prints the results

## Helpful links
- [Scipy Documentation](https://docs.scipy.org/doc/scipy/reference/index.html)
- [Scipy Stats Module Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [mquantiles Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.mquantiles.html)

onelinerhub: [How do I use Python Scipy to calculate quantiles?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-calculate-quantiles)