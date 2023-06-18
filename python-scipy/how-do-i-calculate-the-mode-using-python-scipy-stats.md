# How do I calculate the mode using Python Scipy Stats?
// plain

The `mode` of a dataset is the most frequently occurring value in the dataset. We can use the `mode` function from the `scipy.stats` module to calculate the mode of a dataset in Python.

## Example code

```
from scipy.stats import mode

# Create a dataset
data = [1, 1, 2, 3, 3, 3, 4, 5, 5]

# Calculate the mode
mode(data)
```

## Output example

```
ModeResult(mode=array([3]), count=array([3]))
```

The `mode` function returns a `ModeResult` object which contains two properties:

- `mode`: an array containing the most frequent value in the dataset
- `count`: an array containing the number of occurrences of the most frequent value

In the example above, the mode of the dataset is `3`, which appears `3` times.

## Helpful links
- [Scipy.stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)

onelinerhub: [How do I calculate the mode using Python Scipy Stats?](https://onelinerhub.com/python-scipy/how-do-i-calculate-the-mode-using-python-scipy-stats)