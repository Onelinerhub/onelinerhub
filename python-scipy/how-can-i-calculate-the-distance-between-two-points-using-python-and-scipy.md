# How can I calculate the distance between two points using Python and SciPy?
// plain

The distance between two points can be calculated using Python and SciPy with the following code:

```
from scipy.spatial import distance

point1 = (1, 2)
point2 = (4, 6)

dist = distance.euclidean(point1, point2)

print(dist)
```
This will output ```5.0```.

The code uses the following parts:
- `from scipy.spatial import distance` imports the distance module from SciPy.
- `point1` and `point2` are tuples containing the coordinates of the two points.
- `distance.euclidean(point1, point2)` calculates the Euclidean distance between the two points.
- `print(dist)` prints the distance to the console.

## Helpful links
- [SciPy Spatial Distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
- [Python Tuples](https://www.w3schools.com/python/python_tuples.asp)

onelinerhub: [How can I calculate the distance between two points using Python and SciPy?](https://onelinerhub.com/python-scipy/how-can-i-calculate-the-distance-between-two-points-using-python-and-scipy)