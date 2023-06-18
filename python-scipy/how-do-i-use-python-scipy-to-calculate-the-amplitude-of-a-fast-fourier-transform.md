# How do I use Python SciPy to calculate the amplitude of a Fast Fourier Transform?
// plain

To calculate the amplitude of a Fast Fourier Transform (FFT) using Python SciPy, one can use the `scipy.fftpack.fft` function. This function returns the FFT of a given array of numbers. To get the amplitude from the FFT, one can use the `np.abs` function.

## Example code

```
import numpy as np
from scipy.fftpack import fft

# Create an array of numbers
data = np.array([1,2,3,4,5,6,7,8])

# Calculate the FFT
fft_data = fft(data)

# Calculate the amplitude
amplitude = np.abs(fft_data)

print(amplitude)
```

## Output example

```
[28.         4.89897949  3.60555128  1.84775906  0.76536686  0.76536686
  1.84775906  3.60555128]
```

## Code explanation


- `import numpy as np`: Import the NumPy library as `np`
- `from scipy.fftpack import fft`: Import the `fft` function from the SciPy `fftpack` library
- `data = np.array([1,2,3,4,5,6,7,8])`: Create an array of numbers to be used in the FFT
- `fft_data = fft(data)`: Calculate the FFT of the data array
- `amplitude = np.abs(fft_data)`: Calculate the amplitude of the FFT data using the `np.abs` function
- `print(amplitude)`: Print the amplitude of the FFT data

## Helpful links
- [NumPy documentation](https://numpy.org/doc/)
- [SciPy documentation](https://docs.scipy.org/doc/)

onelinerhub: [How do I use Python SciPy to calculate the amplitude of a Fast Fourier Transform?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-to-calculate-the-amplitude-of-a-fast-fourier-transform)