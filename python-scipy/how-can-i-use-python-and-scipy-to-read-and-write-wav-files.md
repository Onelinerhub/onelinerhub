# How can I use Python and SciPy to read and write WAV files?
// plain

Python and SciPy can be used to read and write WAV files. The `scipy.io.wavfile` module provides functions for reading and writing WAV files.

## Example code

```
from scipy.io import wavfile

# Read the wav file (samplerate, data)
samplerate, data = wavfile.read('file.wav')

# Write the wav file
wavfile.write('file_new.wav', samplerate, data)
```

The `wavfile.read` function reads a WAV file and returns the sample rate and data as a tuple. The sample rate is the number of samples per second and the data is an array of integers representing the amplitude of the sound. The `wavfile.write` function writes a WAV file, taking the sample rate and data as parameters.

## Code explanation

- `from scipy.io import wavfile`: imports the `wavfile` module from the `scipy.io` package
- `samplerate, data = wavfile.read('file.wav')`: reads the WAV file and returns the sample rate and data as a tuple
- `wavfile.write('file_new.wav', samplerate, data)`: writes a WAV file, taking the sample rate and data as parameters

## Helpful links
- [Scipy.io.wavfile documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html)

onelinerhub: [How can I use Python and SciPy to read and write WAV files?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-read-and-write-wav-files)