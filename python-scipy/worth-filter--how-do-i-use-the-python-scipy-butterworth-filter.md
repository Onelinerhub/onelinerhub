# worth filter

How do I use the Python Scipy Butterworth filter?
// plain

A Butterworth filter is a type of signal processing filter designed to have a frequency response as flat as possible in the pass band. It is created using the SciPy library in Python. To use the filter, the following code can be used:

```
from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
```

This code creates two functions, `butter_lowpass` and `butter_lowpass_filter`. The `butter_lowpass` function takes three parameters: `cutoff`, `fs`, and `order`. `cutoff` is the desired cutoff frequency of the filter, `fs` is the sampling frequency of the signal, and `order` is the order of the filter. The `butter_lowpass_filter` function takes four parameters: `data`, `cutoff`, `fs`, and `order`. `data` is the signal to be filtered, and the other parameters are the same as the `butter_lowpass` function.

To use the filter, the following code can be used:

```
# Sample rate and desired cutoff frequencies (in Hz).
fs = 5000.0
cutoff = 500.0

# Sample signal
t = np.linspace(0, 1, 500, endpoint=False)
x = np.sin(2 * np.pi * 300 * t) + 2 * np.sin(2 * np.pi * 600 * t)

# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(x, cutoff, fs, order=6)

plt.subplot(2, 1, 2)
plt.plot(t, y, 'g-', linewidth=2)
plt.xlabel('Time [sec]')
plt.grid()
plt.legend(['Filtered signal'])

plt.subplots_adjust(hspace=0.35)
plt.show()
```

This code creates a signal with two frequencies, 300 Hz and 600 Hz and filters it using the `butter_lowpass_filter` function. The output of this code is:

![alt text](https://i.stack.imgur.com/C2fV4.png)

The code consists of the following parts:
1. Importing the `butter` and `lfilter` functions from the `scipy.signal` library.
2. Creating the `butter_lowpass` function, which takes three parameters: `cutoff`, `fs`, and `order`.
3. Creating the `butter_lowpass_filter` function, which takes four parameters: `data`, `cutoff`, `fs`, and `order`.
4. Creating a signal with two frequencies, 300 Hz and 600 Hz.
5. Filtering the signal using the `butter_lowpass_filter` function.
6. Plotting the original and filtered signals.

## Helpful links
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html

onelinerhub: [worth filter

How do I use the Python Scipy Butterworth filter?](https://onelinerhub.com/python-scipy/worth-filter--how-do-i-use-the-python-scipy-butterworth-filter)