# How do I check which versions of Python are supported by PyTorch?
// plain

PyTorch supports multiple versions of Python, including Python 2.7 and Python 3.5+. To check which versions of Python are supported by PyTorch, you can use the following code:

```
import torch
print(torch.__version__)
```

The output of the above code will be the version of PyTorch installed on your system. To check which versions of Python are supported by this version of PyTorch, you can refer to the [pytorch.org/get-started/previous-versions](https://pytorch.org/get-started/previous-versions) page, which lists the supported Python versions for each version of PyTorch.

For example, if the output of the code above shows that you have PyTorch version 1.4.0 installed, then you can refer to the page to see that Python 2.7 and Python 3.6+ are supported by this version of PyTorch.

## Code explanation


1. `import torch`: This imports the PyTorch library.
2. `print(torch.__version__)`: This prints the version of PyTorch installed on your system.

## Helpful links

- [pytorch.org/get-started/previous-versions](https://pytorch.org/get-started/previous-versions)

onelinerhub: [How do I check which versions of Python are supported by PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-check-which-versions-of-python-are-supported-by-pytorch)