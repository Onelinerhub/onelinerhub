# How do I use the Scipy freqz function in Python?
// plain

The `scipy.signal.freqz` function in Python is used to compute the frequency response of a digital filter. This function takes two arguments: a numerator and denominator polynomial coefficients of a digital filter.

## Example code

```
from scipy.signal import freqz
b = [1, -2, 0.5]
a = [1, 0, 0.3]
w, h = freqz(b, a)
```

The output of the above code is two arrays `w` and `h` which contain the frequency and corresponding complex frequency response of the filter, respectively.

## Code explanation


1. `from scipy.signal import freqz` - imports the `freqz` function from the `scipy.signal` module
2. `b = [1, -2, 0.5]` - defines the numerator polynomial coefficients of the filter
3. `a = [1, 0, 0.3]` - defines the denominator polynomial coefficients of the filter
4. `w, h = freqz(b, a)` - computes the frequency response of the filter using the `freqz` function

## Helpful links

- [Scipy freqz documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html)
- [Digital filter design tutorial](https://www.dspguide.com/ch19/1.htm)

onelinerhub: [How do I use the Scipy freqz function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-the-scipy-freqz-function-in-python)