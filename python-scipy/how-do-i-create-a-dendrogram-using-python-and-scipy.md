# How do I create a dendrogram using Python and SciPy?
// plain

The dendrogram is a graphical representation of a hierarchical structure (e.g. a tree) that is commonly used to represent the relationships between data points in a dataset. It can be created using Python and SciPy with the following steps:

1. Import the necessary libraries:
```
import scipy.cluster.hierarchy as sch
from matplotlib import pyplot as plt
```

2. Create the data to be used in the dendrogram. For example, a 2x3 matrix:
```
data = [[2, 3, 4], [5, 6, 7]]
```

3. Use the SciPy library to generate the linkage matrix:
```
Z = sch.linkage(data, 'ward')
```

4. Generate the dendrogram using the linkage matrix:
```
dendrogram = sch.dendrogram(Z)
```

5. Plot the dendrogram:
```
plt.show()
```

The resulting dendrogram will look like this:

![Dendrogram](https://miro.medium.com/max/1400/1*hCZh_6_2CvH_5FJhXg8K_A.png)

## Helpful links
- [SciPy Hierarchical Clustering and Dendrogram Tutorial](https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/)
- [Complete Guide to Hierarchical Clustering in Python](https://towardsdatascience.com/complete-guide-hierarchical-clustering-in-python-dendrograms-c6d16d8d8c6c)

onelinerhub: [How do I create a dendrogram using Python and SciPy?](https://onelinerhub.com/python-scipy/how-do-i-create-a-dendrogram-using-python-and-scipy)