# How do I use the Python Scipy Bessel function?
// plain

The Scipy Bessel function is a Python library that provides functions for numerical computation of common mathematical functions. It is part of the SciPy library, which is a collection of numerical algorithms and domain-specific toolboxes.

The Bessel function is used to compute the Bessel function of the first kind, which is a solution to the differential equation:

```
x^2 * y'' + x * y' + (x^2 - n^2) * y = 0
```

To use the Bessel function, you can import the library and then call the `scipy.special.jn()` function. This function takes two arguments: the first is the order of the Bessel function, and the second is the value of x. For example, to compute the Bessel function of the first kind at order 0 and x=1, you can run the following code:

```
import scipy.special

scipy.special.jn(0, 1)
# Output: 0.7651976865579666
```

The code above:

1. Imports the scipy.special library
2. Calls the `scipy.special.jn()` function
3. Passes in two arguments: 0 (the order of the Bessel function) and 1 (the value of x)
4. Outputs the result: 0.7651976865579666

For more information, you can refer to the [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.jn.html).

onelinerhub: [How do I use the Python Scipy Bessel function?](https://onelinerhub.com/python-scipy/how-do-i-use-the-python-scipy-bessel-function)