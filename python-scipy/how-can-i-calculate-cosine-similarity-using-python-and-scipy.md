# How can I calculate cosine similarity using Python and SciPy?
// plain

Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. It is defined as the dot product of two vectors divided by the product of their magnitudes.

Using SciPy, cosine similarity can be calculated with the following code:

```
from scipy import spatial

# Define the vectors
a = [1, 2, 3]
b = [4, 5, 6]

# Calculate the cosine similarity
result = 1 - spatial.distance.cosine(a, b)
print(result)
```

## Output example

```
0.974631846197076
```

The code above consists of the following parts:
1. Import the `spatial` module from the SciPy library.
2. Define the two vectors.
3. Calculate the cosine similarity with the `distance.cosine()` method, passing in the two vectors as arguments.
4. Print the result.

## Helpful links
- [SciPy Spatial Distance Functions](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
- [Cosine Similarity - Wikipedia](https://en.wikipedia.org/wiki/Cosine_similarity)

onelinerhub: [How can I calculate cosine similarity using Python and SciPy?](https://onelinerhub.com/python-scipy/how-can-i-calculate-cosine-similarity-using-python-and-scipy)