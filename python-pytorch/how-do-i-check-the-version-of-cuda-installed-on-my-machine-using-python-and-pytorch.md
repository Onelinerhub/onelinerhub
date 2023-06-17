# How do I check the version of CUDA installed on my machine using Python and PyTorch?
// plain

To check the version of CUDA installed on your machine using Python and PyTorch, you can use the following code:

```python
import torch
print(torch.version.cuda)
```

This will print out the version of CUDA installed on the machine, for example:
```
10.1
```

The code consists of the following parts:

1. `import torch` imports the PyTorch library to access the version information.
2. `print(torch.version.cuda)` prints out the version of CUDA installed on the machine.

For more information about the PyTorch version information, you can refer to the [PyTorch documentation](https://pytorch.org/docs/stable/torch.html#version-info).

onelinerhub: [How do I check the version of CUDA installed on my machine using Python and PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-check-the-version-of-cuda-installed-on-my-machine-using-python-and-pytorch)