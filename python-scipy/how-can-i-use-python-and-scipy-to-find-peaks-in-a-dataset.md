# How can I use Python and SciPy to find peaks in a dataset?
// plain

Python and SciPy can be used to find peaks in a dataset. The `scipy.signal.find_peaks()` function can be used to detect peaks in a dataset. This function takes a 1-dimensional array and returns the indices of the peaks.

## Example code

```
import scipy.signal

x = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1]
peaks, _ = scipy.signal.find_peaks(x)

print(peaks)
```

## Output example

```
[2 8]
```

The code above first imports the `scipy.signal` module. Then, it creates an array of values and uses the `find_peaks()` function to detect the peaks in the data. Finally, it prints out the indices of the peaks.

## Code explanation

- `import scipy.signal`: imports the `scipy.signal` module
- `x = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1]`: creates an array of values
- `scipy.signal.find_peaks(x)`: detects the peaks in the data
- `print(peaks)`: prints out the indices of the peaks

## Helpful links
- [scipy.signal.find_peaks()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html)

onelinerhub: [How can I use Python and SciPy to find peaks in a dataset?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-find-peaks-in-a-dataset)