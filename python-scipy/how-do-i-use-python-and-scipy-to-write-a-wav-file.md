# How do I use Python and SciPy to write a WAV file?
// plain

To write a WAV file with Python and SciPy, you can use the `scipy.io.wavfile.write` function. This example code will create a WAV file with a sine wave of frequency 440 Hz and a duration of 2 seconds:

```
import scipy.io.wavfile
import numpy as np

# Sampling rate of the sine wave
sampling_rate = 44100.0

# Duration of the sine wave
duration = 2.0

# Sine wave frequency
frequency = 440.0

# Generate time points
time_points = np.linspace(0, duration, int(sampling_rate * duration))

# Generate sine wave
sine_wave = np.sin(frequency * time_points * 2 * np.pi)

# Convert to 16-bit data
sine_wave = np.int16(sine_wave * 32767)

# Write the WAV file
scipy.io.wavfile.write("sine_wave.wav", sampling_rate, sine_wave)
```

This code will create a WAV file called `sine_wave.wav` in the current directory.

The code consists of the following parts:

1. Import the necessary modules: `scipy.io.wavfile` and `numpy`.
2. Set the sampling rate, duration, and frequency of the sine wave.
3. Generate the time points for the sine wave.
4. Generate the sine wave.
5. Convert the sine wave to 16-bit data.
6. Write the WAV file.

For more information, see the [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html).

onelinerhub: [How do I use Python and SciPy to write a WAV file?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-write-a-wav-file)