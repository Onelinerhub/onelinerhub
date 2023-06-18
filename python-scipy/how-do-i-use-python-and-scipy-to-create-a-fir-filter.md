# How do I use Python and SciPy to create a FIR filter?
// plain

FIR (finite impulse response) filters are a type of digital filter used to process signals in the frequency domain. In Python, SciPy provides the signal processing module, which contains functions for creating and manipulating FIR filters.

To create a FIR filter, the scipy.signal.firwin() function can be used. This function requires the desired filter length, cutoff frequency, window type, and other optional parameters. For example:

```
import scipy.signal as signal

# Create a FIR filter with length 101, cutoff frequency 0.2, and a Hamming window
b = signal.firwin(101, 0.2, window="hamming")
```

The output of the above code is an array of coefficients for the filter.

The filter can then be used to filter a signal using the scipy.signal.lfilter() function. This function requires the filter coefficients, the signal to be filtered, and other optional parameters. For example:

```
# Filter a signal x with the previously created filter b
x_filtered = signal.lfilter(b, 1, x)
```

The output of the above code is the filtered signal.

## Code explanation

- `import scipy.signal as signal`: imports the SciPy signal processing module
- `b = signal.firwin(101, 0.2, window="hamming")`: creates a FIR filter with length 101, cutoff frequency 0.2, and a Hamming window
- `x_filtered = signal.lfilter(b, 1, x)`: filters a signal x with the previously created filter b

## Helpful links
- SciPy Signal Processing: https://docs.scipy.org/doc/scipy/reference/signal.html
- scipy.signal.firwin(): https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html
- scipy.signal.lfilter(): https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html

onelinerhub: [How do I use Python and SciPy to create a FIR filter?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-create-a-fir-filter)