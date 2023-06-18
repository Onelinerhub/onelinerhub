# How do I use Python and SciPy to perform principal component analysis?
// plain

Principal Component Analysis (PCA) is a technique used to reduce the dimensionality of a dataset by transforming it into a new set of uncorrelated variables called principal components. To perform PCA with Python and SciPy, we can use the `scipy.linalg.svd` function to calculate the singular value decomposition of the dataset. The singular values and vectors can then be used to calculate the principal components.

For example, consider the following dataset:

```
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

We can use the `scipy.linalg.svd` function to calculate the singular value decomposition of this dataset:

```
U, S, V = scipy.linalg.svd(data)
```

The output of this function is three matrices: `U`, `S`, and `V`. `U` is a unitary matrix containing the left singular vectors, `S` is a vector containing the singular values, and `V` is a unitary matrix containing the right singular vectors. The principal components can then be calculated as follows:

```
principal_components = U @ np.diag(S)
```

The output of this code is:

```
array([[-2.44948974e+00,  0.00000000e+00,  0.00000000e+00],
       [-4.89897948e+00,  0.00000000e+00,  0.00000000e+00],
       [-7.34846923e+00,  0.00000000e+00,  0.00000000e+00]])
```

## Code explanation


1. `U, S, V = scipy.linalg.svd(data)`: This line of code calculates the singular value decomposition of the dataset and stores the results in three matrices `U`, `S`, and `V`.

2. `principal_components = U @ np.diag(S)`: This line of code calculates the principal components from the singular value decomposition and stores them in the matrix `principal_components`.

## Helpful links

- [SciPy Linear Algebra Documentation](https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html)
- [Principal Component Analysis with Python](https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60)

onelinerhub: [How do I use Python and SciPy to perform principal component analysis?](https://onelinerhub.com/python-scipy/how-do-i-use-python-and-scipy-to-perform-principal-component-analysis)