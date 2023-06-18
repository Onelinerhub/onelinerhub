# How can I use Python and SciPy to create a low pass filter?
// plain

In order to create a low pass filter using Python and SciPy, the following steps should be taken:

1. Import the necessary libraries:
```python
import numpy as np
from scipy import signal
```

2. Create the low-pass filter. This can be done by using the `signal.butter` function, which takes three parameters:
    - `N`: The order of the filter
    - `Wn`: The cutoff frequency of the filter, normalized from 0 to 1 (1 being the Nyquist frequency)
    - `btype`: The type of filter, in this case ‘lowpass’

```python
b, a = signal.butter(N=4, Wn=0.2, btype='lowpass')
```

3. Use the filter to filter a signal. This can be done by using the `signal.lfilter` function, which takes three parameters:
    - `b`: The numerator coefficient array of the filter
    - `a`: The denominator coefficient array of the filter
    - `x`: The signal to be filtered

```python
x = np.linspace(0, 10, num=1000)
y = signal.lfilter(b, a, x)
```

4. Plot the filtered signal. This can be done by using the `matplotlib.pyplot` library:

```python
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
```

## Helpful links

- [Scipy Signal Butter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html)
- [Scipy Signal Lfilter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html)
- [Matplotlib Pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html)

onelinerhub: [How can I use Python and SciPy to create a low pass filter?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-create-a-low-pass-filter)