# How can I use Python and SciPy to perform a Fast Fourier Transform?
// plain

The Fast Fourier Transform (FFT) is a powerful tool for analyzing signals in the frequency domain. Python and SciPy provide an easy way to perform FFTs. To use SciPy, the following code can be used:

```
import numpy as np
from scipy.fftpack import fft

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
```

This code will create an array of 600 points, spaced 1/800 apart, and create a signal consisting of two sinusoidal waves. The FFT is then applied to the signal with the `fft` function from SciPy's `fftpack` submodule.

The output of the FFT is an array of complex numbers, representing the amplitude and phase of each frequency component in the signal. To get the power spectrum of the signal, the magnitude of each complex number can be taken with the `np.abs` function.

```
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
```

This code will plot the power spectrum of the signal.

## Code explanation
**

1. `import numpy as np`: imports the numpy library.
2. `from scipy.fftpack import fft`: imports the `fft` function from SciPy's `fftpack` submodule.
3. `N = 600`: sets the number of sample points.
4. `T = 1.0 / 800.0`: sets the sample spacing.
5. `x = np.linspace(0.0, N*T, N)`: creates an array of 600 points, spaced 1/800 apart.
6. `y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)`: creates a signal consisting of two sinusoidal waves.
7. `yf = fft(y)`: applies the FFT to the signal.
8. `xf = np.linspace(0.0, 1.0/(2.0*T), N//2)`: creates an array of frequencies.
9. `plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))`: plots the power spectrum of the signal.

**## Helpful links**

- [Python FFT Tutorial](https://www.tutorialspoint.com/scipy/scipy_fftpack.htm)
- [SciPy FFT Documentation](https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html)

onelinerhub: [How can I use Python and SciPy to perform a Fast Fourier Transform?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-perform-a-fast-fourier-transform)