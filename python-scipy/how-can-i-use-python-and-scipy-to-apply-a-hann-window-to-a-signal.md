# How can I use Python and SciPy to apply a Hann window to a signal?
// plain

To apply a Hann window to a signal using Python and SciPy, you can use the `signal.hann()` function. This function takes in a signal array and returns the windowed signal array. For example:

```
import numpy as np
from scipy import signal

# Generate a signal
t = np.linspace(0, 1, 500, endpoint=False)
sig = np.sin(2 * np.pi * 5 * t)

# Apply a Hann window
win = signal.hann(500)
filtered = sig * win

# Print the filtered signal
print(filtered)
```

The output of the above code would be an array of the windowed signal.

The code consists of the following parts:
1. Importing the necessary packages (`numpy` and `scipy.signal`).
2. Generating a signal (`sig`) with `np.linspace()` and `np.sin()`.
3. Applying the Hann window (`win`) to the signal with `signal.hann()`.
4. Multiplying the signal and the window to get the filtered signal (`filtered`).
5. Printing out the filtered signal.

## Helpful links
- [SciPy signal.hann() documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hann.html)
- [Python numpy.linspace() documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)
- [Python numpy.sin() documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html)

onelinerhub: [How can I use Python and SciPy to apply a Hann window to a signal?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-apply-a-hann-window-to-a-signal)