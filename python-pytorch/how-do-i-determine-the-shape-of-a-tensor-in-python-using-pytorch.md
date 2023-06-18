# How do I determine the shape of a tensor in Python using PyTorch?
// plain

To determine the shape of a tensor in Python using PyTorch, we can use the `shape` attribute of the tensor. For example, given a tensor `x`:

```
import torch

x = torch.randn(2, 3)
```

We can use the `shape` attribute to determine its shape:

```
print(x.shape)
```

## Output example

```
torch.Size([2, 3])
```

The `shape` attribute returns a `torch.Size` object, which is a tuple of the dimensions of the tensor. In this example, `x` has two dimensions, with the first dimension having a size of 2 and the second dimension having a size of 3.

## Code explanation

- `import torch`: imports the PyTorch library
- `x = torch.randn(2, 3)`: creates a tensor `x` with two dimensions of size 2 and 3 respectively
- `print(x.shape)`: prints the shape of the tensor `x`

## Helpful links
- https://pytorch.org/docs/stable/tensors.html
- https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py

onelinerhub: [How do I determine the shape of a tensor in Python using PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-determine-the-shape-of-a-tensor-in-python-using-pytorch)