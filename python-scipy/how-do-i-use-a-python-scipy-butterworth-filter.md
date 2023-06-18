# How do I use a Python Scipy Butterworth filter?
// plain

To use a Python Scipy Butterworth filter, the following steps should be taken:
1. Import the necessary modules:
```
import scipy.signal as signal
import numpy as np
```
2. Create a signal. For example, a sine wave:
```
fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / float(fs)
x = amp*np.sin(2*np.pi*freq*time)
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
```
3. Create a Butterworth filter of order 3, with a cutoff frequency of 700 Hz:
```
b, a = signal.butter(3, 700/(fs/2), btype='low')
```
4. Apply the filter to the signal:
```
filtered_x = signal.lfilter(b, a, x)
```
5. Plot the original and filtered signals:
```
import matplotlib.pyplot as plt
plt.plot(time, x, label='Noisy signal')
plt.plot(time, filtered_x, label='Filtered signal (%g Hz)' % f0)
plt.xlabel('time (seconds)')
plt.hlines([-amp, amp], 0, time[-1], linestyles='--')
plt.grid(True)
plt.axis('tight')
plt.legend(loc='upper left')
plt.show()
```

## Code explanation
**
1. `import scipy.signal as signal`: This imports the `signal` module from the `scipy` package, which contains functions for signal processing.
2. `import numpy as np`: This imports the `numpy` package, which provides useful functions for array manipulation.
3. `fs = 10e3`: This sets the sampling frequency of the signal to 10 kHz.
4. `N = 1e5`: This sets the number of samples in the signal to 100,000.
5. `amp = 2*np.sqrt(2)`: This sets the amplitude of the signal to 2√2.
6. `freq = 1234.0`: This sets the frequency of the signal to 1234 Hz.
7. `noise_power = 0.001 * fs / 2`: This sets the power of the noise to 0.001 times the sampling frequency divided by 2.
8. `time = np.arange(N) / float(fs)`: This creates an array of N samples, evenly spaced in time, with the sampling frequency set to fs.
9. `x = amp*np.sin(2*np.pi*freq*time)`: This creates a sine wave with the given amplitude, frequency, and sampling frequency.
10. `x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)`: This adds random noise to the signal with the given noise power.
11. `b, a = signal.butter(3, 700/(fs/2), btype='low')`: This creates a Butterworth filter of order 3 and cutoff frequency of 700 Hz.
12. `filtered_x = signal.lfilter(b, a, x)`: This applies the filter to the signal.
13. `import matplotlib.pyplot as plt`: This imports the `matplotlib` package, which provides functions for plotting.
14. `plt.plot(time, x, label='Noisy signal')`: This plots the noisy signal.
15. `plt.plot(time, filtered_x, label='Filtered signal (%g Hz)' % f0)`: This plots the filtered signal.
16. `plt.xlabel('time (seconds)')`: This sets the x-axis label to "time (seconds)".
17. `plt.hlines([-amp, amp], 0, time[-1], linestyles='--')`: This plots horizontal lines at the given amplitudes.
18. `plt.grid(True)`: This turns on the grid.
19. `plt.axis('tight')`: This sets the axis limits to the range of the data.
20. `plt.legend(loc='upper left')`: This adds a legend to the plot.
21. `plt.show()`: This displays the plot.

**Relevant Links**
- [Scipy Signal Processing](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [Numpy Reference](https://numpy.org/doc/stable/reference/)
- [Matplotlib Tutorial](https://matplotlib.org/tutorials/index.html)

onelinerhub: [How do I use a Python Scipy Butterworth filter?](https://onelinerhub.com/python-scipy/how-do-i-use-a-python-scipy-butterworth-filter)