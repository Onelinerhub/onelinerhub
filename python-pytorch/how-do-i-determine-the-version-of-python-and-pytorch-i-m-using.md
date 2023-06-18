# How do I determine the version of Python and PyTorch I'm using?
// plain

You can determine the version of Python and PyTorch you are using by running the following code:

```
import sys
import torch

print('Python version:', sys.version)
print('PyTorch version:', torch.__version__)
```

## Output example

```
Python version: 3.7.7 (default, Mar 10 2020, 15:43:33)
[Clang 11.0.0 (clang-1100.0.33.17)]
PyTorch version: 1.5.1+cu101
```

The code is composed of the following parts:

1. `import sys` - This imports the `sys` module, which provides access to information about the Python interpreter.

2. `import torch` - This imports the `torch` module, which provides access to PyTorch functions and classes.

3. `print('Python version:', sys.version)` - This prints the version of Python being used.

4. `print('PyTorch version:', torch.__version__)` - This prints the version of PyTorch being used.

## Helpful links

- [Python Documentation: sys Module](https://docs.python.org/3/library/sys.html)
- [PyTorch Documentation: torch Module](https://pytorch.org/docs/stable/torch.html)

onelinerhub: [How do I determine the version of Python and PyTorch I'm using?](https://onelinerhub.com/python-pytorch/how-do-i-determine-the-version-of-python-and-pytorch-i-m-using)