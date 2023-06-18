# How do I use Python and SciPy to apply a high pass filter?
// plain

The SciPy library provides a variety of functions for applying high pass filters. To use Python and SciPy to apply a high pass filter, first import the necessary SciPy library functions:

```
from scipy import signal
```

Next, define the filter parameters. For example, to create a high pass filter with a cutoff frequency of 0.1 Hz and a filter order of 4:

```
cutoff = 0.1
order = 4
```

Then, use the `butter` function from the `signal` module to create the filter:

```
b, a = signal.butter(order, cutoff, btype='highpass')
```

Finally, apply the filter to a given signal using the `lfilter` function from the `signal` module:

```
filtered_signal = signal.lfilter(b, a, signal)
```

The `filtered_signal` will contain the filtered signal with the high pass filter applied.

## Code explanation


- `from scipy import signal`: imports the SciPy library functions necessary for applying high pass filters.
- `cutoff = 0.1`: defines the cutoff frequency of the filter.
- `order = 4`: defines the filter order.
- `b, a = signal.butter(order, cutoff, btype='highpass')`: creates the filter.
- `filtered_signal = signal.lfilter(b, a, signal)`: applies the filter to the given signal.

## Helpful links

- [scipy.signal.butter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html)
- [scipy.signal.lfilter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html)

onelinerhub: [How do I use Python and SciPy to apply a high pass filter?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-apply-a-high-pass-filter)