# How can I use Python and SciPy to find the root of a function?
// plain

Python and SciPy can be used to find the root of a function using the `scipy.optimize.root` function. This function uses a variety of algorithms to find the root of a given function. To find the root of a function, the function must be defined and passed to the `scipy.optimize.root` function.

For example, to find the root of the function `f(x) = x^2 - 4`, it can be coded as follows:

```python
import scipy.optimize as opt

def f(x):
    return x**2 - 4

root = opt.root(f, [1])

print(root.x)
```

## Output example

```
[2.]
```

1. `import scipy.optimize as opt`: imports the SciPy optimize module as `opt`.
2. `def f(x):`: defines the function to find the root of.
3. `root = opt.root(f, [1])`: uses the `opt.root` function to find the root of the function `f(x)` starting at `x=1`.
4. `print(root.x)`: prints the root of the function.

## Helpful links
- [SciPy Optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [SciPy Optimize Root](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html)

onelinerhub: [How can I use Python and SciPy to find the root of a function?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-find-the-root-of-a-function)