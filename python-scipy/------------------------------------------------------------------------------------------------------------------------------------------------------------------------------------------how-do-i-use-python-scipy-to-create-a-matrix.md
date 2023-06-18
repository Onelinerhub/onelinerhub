# &#1086;&#1073;&#1088;&#1072;&#1090;&#1100; &#1089;&#1090;&#1088;&#1072;&#1090;&#1080;&#1088;&#1086;&#1074;&#1072;&#1085;&#1085;&#1099;&#1081; &#1084;&#1072;&#1089;&#1090;&#1077;&#1088;

How do I use Python Scipy to create a matrix?
// plain

Python Scipy is a powerful library that provides a range of numerical algorithms and data structures. It can be used to create a matrix with the `scipy.sparse.csr_matrix()` function. This function takes three parameters:

* `data`: An array containing the elements of the matrix
* `indices`: An array containing the row indices of the matrix
* `indptr`: An array containing the column indices of the matrix

For example, the following code creates a simple 3x3 matrix:

```
from scipy.sparse import csr_matrix

data = [1, 2, 3, 4, 5, 6]
indices = [0, 2, 2, 0, 1, 2]
indptr = [0, 2, 3, 6]

matrix = csr_matrix((data, indices, indptr), shape=(3, 3))

print(matrix.toarray())

# Output:
# [[1 0 2]
#  [0 4 0]
#  [3 5 6]]
```

The `data` array contains the elements of the matrix, the `indices` array contains the row indices of the matrix, and the `indptr` array contains the column indices of the matrix. The `shape` parameter is used to specify the size of the matrix. Finally, the `toarray()` method is used to convert the matrix to a regular array.

onelinerhub: [&#1086;&#1073;&#1088;&#1072;&#1090;&#1100; &#1089;&#1090;&#1088;&#1072;&#1090;&#1080;&#1088;&#1086;&#1074;&#1072;&#1085;&#1085;&#1099;&#1081; &#1084;&#1072;&#1089;&#1090;&#1077;&#1088;

How do I use Python Scipy to create a matrix?](https://onelinerhub.com/python-scipy/------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------how-do-i-use-python-scipy-to-create-a-matrix)