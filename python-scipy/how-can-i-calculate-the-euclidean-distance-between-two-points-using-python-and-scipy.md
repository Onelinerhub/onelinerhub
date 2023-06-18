# How can I calculate the Euclidean distance between two points using Python and SciPy?
// plain

The Euclidean distance between two points can be calculated using Python and SciPy. The following example code block will calculate the Euclidean distance between two points `(x1, y1)` and `(x2, y2)`:

```
from scipy.spatial import distance
x1 = 5
y1 = 6
x2 = 3
y2 = 4
euclidean_distance = distance.euclidean((x1, y1), (x2, y2))
print(euclidean_distance)
```
The output of this code will be:
```
2.8284271247461903
```

The code can be broken down into the following parts:

1. `from scipy.spatial import distance`: This imports the `distance` module from SciPy.
2. `x1 = 5` and `y1 = 6`: These set the x and y coordinates of the first point.
3. `x2 = 3` and `y2 = 4`: These set the x and y coordinates of the second point.
4. `euclidean_distance = distance.euclidean((x1, y1), (x2, y2))`: This calculates the Euclidean distance between the two points.
5. `print(euclidean_distance)`: This prints the result of the calculation.

## Helpful links
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/reference/index.html)
- [SciPy Spatial Distance Documentation](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)

onelinerhub: [How can I calculate the Euclidean distance between two points using Python and SciPy?](https://onelinerhub.com/python-scipy/how-can-i-calculate-the-euclidean-distance-between-two-points-using-python-and-scipy)