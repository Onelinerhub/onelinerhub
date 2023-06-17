# How do I use the Python bindings for PyTorch?
// plain

PyTorch provides Python bindings for easily writing neural network layers in Python code. To use the Python bindings for PyTorch, you must first install the PyTorch package from PyPI:

```
pip install torch
```

Then you can import the `torch` package into your code and start using it:

```python
import torch

# Create a tensor
x = torch.rand(5, 3)
print(x)
```

```
tensor([[0.5604, 0.2538, 0.1654],
        [0.7462, 0.7195, 0.7274],
        [0.9071, 0.9553, 0.8167],
        [0.4599, 0.9845, 0.3122],
        [0.9185, 0.7109, 0.9100]])
```

The `torch` package provides a number of functions for creating and manipulating tensors, such as `torch.rand()` for creating random tensors and `torch.sum()` for summing tensors. You can also use the `torch.nn` package for building neural networks.

For more information, see the [PyTorch documentation](https://pytorch.org/docs/stable/index.html).

onelinerhub: [How do I use the Python bindings for PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-use-the-python-bindings-for-pytorch)