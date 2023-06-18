# How do I use Python Scipy Linkage to cluster data?
// plain

To use Python Scipy Linkage to cluster data, you must first import the necessary libraries:

```
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
```

Next, you must create a dataset, which can be done with the following code:

```
data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
```

Then, you can use the `linkage` function to generate the hierarchical clustering:

```
Z = linkage(data, 'ward')
```

The `dendrogram` function can then be used to create a visualization of the hierarchical clustering:

```
dendrogram(Z)
```

The output of the `dendrogram` function is a visualization of the hierarchical clustering:

![dendrogram](https://i.imgur.com/9caUQ6m.png)

## Code explanation

- `import numpy as np`: imports the `numpy` library and assigns it to the alias `np`
- `from scipy.cluster.hierarchy import linkage, dendrogram`: imports the `linkage` and `dendrogram` functions from the `scipy` library
- `data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])`: creates an array of data points
- `Z = linkage(data, 'ward')`: performs hierarchical clustering on the data points using the `ward` method
- `dendrogram(Z)`: creates a visualization of the hierarchical clustering

## Helpful links
- [Scipy Hierarchical Clustering and Dendrogram Tutorial](https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/)
- [Clustering with SciPy](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)

onelinerhub: [How do I use Python Scipy Linkage to cluster data?](https://onelinerhub.com/python-scipy/how-do-i-use-python-scipy-linkage-to-cluster-data)