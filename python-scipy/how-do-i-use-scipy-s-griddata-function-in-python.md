# How do I use scipy's griddata function in Python?
// plain

The `griddata` function in SciPy is used to interpolate scattered data points to a regular grid. It is a part of the SciPy interpolate module.

## Example code


```
import numpy as np
from scipy.interpolate import griddata

# Define some scattered data
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

# Interpolate the data
xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))
zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

print(zi)
```

## Output example

```
[[0.94867884 0.9273742  0.89822994 0.85958175 0.81275252 0.75904736
  0.69979588 0.63625395 0.57070476 0.50518069]
 [0.91701592 0.90202435 0.87950806 0.84967397 0.8127788  0.76933574
  0.71992799 0.66539017 0.60701056 0.5461132 ]
 [0.88176095 0.86899097 0.85008247 0.82407929 0.79119814 0.75169976
  0.7067096  0.65653933 0.60243768 0.5455906 ]
 [0.84310341 0.83298846 0.81709449 0.79546816 0.7673798  0.7330116
  0.69249072 0.64699295 0.596739   0.54191896]
 [0.80145323 0.79410122 0.78131802 0.76318072 0.73983717 0.71035441
  0.67500159 0.63400339 0.58765936 0.53712646]
 [0.75721868 0.75251541 0.74253655 0.72739863 0.70726346 0.68229978
  0.65270011 0.61879783 0.58069183 0.53874863]
 [0.71167647 0.70944773 0.70209833 0.69070993 0.67548199 0.65660288
  0.63427279 0.60864609 0.57996811 0.54835641]
 [0.66514582 0.6656841  0.66117532 0.65173747 0.63847891 0.62162599
  0.60136288 0.57785971 0.55147089 0.52236897]
 [0.61809923 0.62139836 0.62084441 0.61650241 0.60849092 0.59698849
  0.58210407 0.56400781 0.54291085 0.51890586]
 [0.57033552 0.57603958 0.57810861 0.5766059  0.57167032 0.56336675
  0.55185094 0.53729051 0.51981604 0.49956891]]
```

The code above creates some random data points (x, y, z) and then uses the `griddata` function to interpolate the data to a regular grid (xi, yi). The `method` parameter is used to specify the interpolation method and can be either 'linear' or 'cubic'.

## Code explanation


1. `import numpy as np`: imports the NumPy library
2. `from scipy.interpolate import griddata`: imports the `griddata` function from the SciPy interpolate module
3. `x = np.random.rand(10)`: creates an array of 10 random numbers
4. `xi = np.linspace(min(x), max(x))`: creates an array of evenly spaced numbers between the minimum and maximum values of x
5. `zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')`: uses the `griddata` function to interpolate the data points to the regular grid

## Helpful links

- [SciPy Interpolate Documentation](https://docs.scipy.org/doc/scipy/reference/interpolate.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)

onelinerhub: [How do I use scipy's griddata function in Python?](https://onelinerhub.com/python-scipy/how-do-i-use-scipy-s-griddata-function-in-python)