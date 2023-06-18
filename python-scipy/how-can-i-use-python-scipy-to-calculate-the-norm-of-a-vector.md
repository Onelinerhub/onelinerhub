# How can I use python scipy to calculate the norm of a vector?
// plain

Using Python Scipy, the norm of a vector can be calculated using the `la.norm` function. This function takes in three parameters, the vector, the order of the norm (default is 2) and an axis (default is None).

## Example code

```
import scipy.linalg as la

vector = [1,2,3,4]
result = la.norm(vector)

print(result)
```
## Output example

```
5.477225575051661
```

The code consists of the following parts:
1. Importing the `scipy.linalg` module as `la` - This imports the module and gives it the alias `la`, which will be used to call the `norm` function.
2. Creating the vector - This creates a vector of 4 elements.
3. Calculating the norm - This uses the `la.norm` function to calculate the norm of the vector. This function takes in three parameters, the vector, the order of the norm (default is 2) and an axis (default is None).
4. Printing the result - This prints the result of the calculation.

## Helpful links
- [Scipy Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html)

onelinerhub: [How can I use python scipy to calculate the norm of a vector?](https://onelinerhub.com/python-scipy/how-can-i-use-python-scipy-to-calculate-the-norm-of-a-vector)