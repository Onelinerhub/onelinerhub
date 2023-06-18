# How do I check the Python version requirements for PyTorch?
// plain

To check the Python version requirements for PyTorch, you can use the `torch.version.__version__` command. This command will return a string indicating the version of PyTorch installed on your machine.

For example, if you have PyTorch version 1.7.1 installed, the following code will return `1.7.1`:
```python
import torch
print(torch.version.__version__)
```
## Output example

```
1.7.1
```

You can also check the version of Python installed on your machine by using the `sys.version` command. This command will return a string indicating the version of Python installed on your machine.

For example, if you have Python version 3.8.5 installed, the following code will return `3.8.5`:
```python
import sys
print(sys.version)
```
## Output example

```
3.8.5
```

PyTorch requires Python version 3.6 or higher. Therefore, you should ensure that the version of Python returned by `sys.version` is 3.6 or higher.

## Helpful links
- [PyTorch Docs - Installing PyTorch](https://pytorch.org/get-started/locally/)
- [Python Docs - sys — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)

onelinerhub: [How do I check the Python version requirements for PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-check-the-python-version-requirements-for-pytorch)