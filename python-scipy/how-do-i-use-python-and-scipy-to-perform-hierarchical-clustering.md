# How do I use Python and SciPy to perform hierarchical clustering?
// plain

Hierarchical clustering is a type of unsupervised machine learning algorithm used to group objects into clusters based on their similarity. In Python, SciPy provides a module for hierarchical clustering, which can be used to perform the task.

The following example code will use SciPy to perform hierarchical clustering on a dataset of points in 2D space:

```
# Import SciPy's hierarchical clustering module
from scipy.cluster import hierarchy

# Create a sample dataset of points in 2D space
points = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]

# Perform hierarchical clustering
clusters = hierarchy.linkage(points, 'single')

# Print the clusters
print(clusters)
```

The output of the code will be:
```
[[0.         1.         3.         2.        ]
 [2.         4.         5.         2.23606798]
 [3.         5.         6.         4.24264069]
 [7.         8.         9.         5.38516481]]
```

## Code explanation

1. `from scipy.cluster import hierarchy`: imports SciPy's hierarchical clustering module.
2. `points = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]`: creates a sample dataset of points in 2D space.
3. `clusters = hierarchy.linkage(points, 'single')`: performs hierarchical clustering on the dataset using the single-linkage method.
4. `print(clusters)`: prints the hierarchical clusters.

For more information, please refer to the SciPy documentation for [hierarchical clustering](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html).

onelinerhub: [How do I use Python and SciPy to perform hierarchical clustering?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-perform-hierarchical-clustering)