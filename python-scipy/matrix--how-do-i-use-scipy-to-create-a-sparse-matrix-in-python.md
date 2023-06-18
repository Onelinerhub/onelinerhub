# matrix

How do I use SciPy to create a sparse matrix in Python?
// plain

SciPy is a Python library that provides functions for scientific computing. It includes a module for working with sparse matrices, which are matrices that have a large number of elements, most of which are zero. To create a sparse matrix using SciPy, you can use the `scipy.sparse.csr_matrix` function. This function takes three arguments: `data`, `indices`, and `indptr`.

The `data` argument is a one-dimensional array containing the non-zero elements of the matrix. The `indices` argument is an array of the column indices for each non-zero element. The `indptr` argument is an array of indices that indicate the start of a row in the `data` array.

For example, to create a sparse matrix with the following values:

|  | 0 | 1 | 2 |
|---|---|---|---|
| 0 | 1 | 0 | 0 |
| 1 | 0 | 2 | 0 |
| 2 | 0 | 0 | 3 |

You could use the following code:

```
import scipy.sparse

data = [1, 2, 3]
indices = [0, 1, 2]
indptr = [0, 1, 3, 3]

matrix = scipy.sparse.csr_matrix((data, indices, indptr))

print(matrix.toarray())
```

The output of this code would be:

```
[[1 0 0]
 [0 2 0]
 [0 0 3]]
```

The code consists of the following parts:

* `import scipy.sparse` imports the SciPy sparse module.
* `data = [1, 2, 3]` creates an array containing the non-zero elements of the matrix.
* `indices = [0, 1, 2]` creates an array containing the column indices for each element.
* `indptr = [0, 1, 3, 3]` creates an array containing indices that indicate the start of a row in the `data` array.
* `matrix = scipy.sparse.csr_matrix((data, indices, indptr))` creates a sparse matrix using the `data`, `indices`, and `indptr` arrays.
* `print(matrix.toarray())` prints the matrix as a dense array.

## Helpful links

* [SciPy Sparse Matrices Documentation](https://docs.scipy.org/doc/scipy/reference/sparse.html)
* [SciPy Sparse Matrix Examples](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix)

onelinerhub: [matrix

How do I use SciPy to create a sparse matrix in Python?](https://onelinerhub.com/python-scipy/matrix--how-do-i-use-scipy-to-create-a-sparse-matrix-in-python)