# How do I use the fftshift function in Python SciPy?
// plain

The `fftshift` function in Python SciPy allows you to shift the zero-frequency component of a Fourier Transform to the center of the array. This is useful for plotting the FFT in a more intuitive manner.

## Example code

```
import numpy as np
from scipy.fftpack import fftshift

# Generate a test signal
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Perform FFT
f = np.fft.fft(y)

# Shift the FFT
fshift = fftshift(f)
```

The output of the above code is an array of complex numbers, `fshift`, which is the shifted Fourier Transform of the input signal.

## Code explanation


1. `import numpy as np`: This imports the NumPy library, which is used for numerical computing.
2. `from scipy.fftpack import fftshift`: This imports the `fftshift` function from the SciPy library.
3. `x = np.linspace(0, 10, 100)`: This generates a test signal of 100 equally spaced points from 0 to 10.
4. `y = np.sin(x)`: This creates a sine wave from the test signal.
5. `f = np.fft.fft(y)`: This performs a Fourier Transform on the sine wave.
6. `fshift = fftshift(f)`: This shifts the zero-frequency component of the Fourier Transform to the center of the array.

## Helpful links
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/)

onelinerhub: [How do I use the fftshift function in Python SciPy?](https://onelinerhub.com/python-scipy/how-do-i-use-the-fftshift-function-in-python-scipy)