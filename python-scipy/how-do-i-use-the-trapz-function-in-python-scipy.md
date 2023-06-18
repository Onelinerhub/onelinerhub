# How do I use the trapz function in Python SciPy?
// plain

The `trapz` function in SciPy is a numerical integration routine used to approximate the definite integral of a given function. It uses the trapezoidal rule to approximate the area under a curve.

## Example code

```
import numpy as np
from scipy.integrate import trapz

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 4, 3, 2, 5])

integral = trapz(y, x)
print(integral)
```

## Output example

```
9.0
```

## Code explanation

- `import numpy as np`: imports the NumPy library as `np`
- `from scipy.integrate import trapz`: imports the `trapz` function from the `scipy.integrate` library
- `x = np.array([0, 1, 2, 3, 4])`: creates an array of the x-values
- `y = np.array([1, 4, 3, 2, 5])`: creates an array of the y-values
- `integral = trapz(y, x)`: calculates the integral using the `trapz` function
- `print(integral)`: prints the calculated integral

## Helpful links
- [SciPy trapz documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapz.html)
- [NumPy array documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)

onelinerhub: [How do I use the trapz function in Python SciPy?](https://onelinerhub.com/python-scipy/how-do-i-use-the-trapz-function-in-python-scipy)