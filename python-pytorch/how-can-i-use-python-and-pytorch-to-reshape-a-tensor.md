# How can I use Python and PyTorch to reshape a tensor?
// plain

The `reshape` function in the PyTorch library is used to reshape a tensor. It takes a tuple as an argument, which specifies the desired shape of the tensor. The following example shows how to use `reshape` to reshape a tensor from a 3x3 matrix to a 9x1 vector.

```
import torch

# Create a 3x3 matrix
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Reshape to a 9x1 vector
y = x.reshape(9, 1)

print(y)
```

## Output example

```
tensor([[1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9]])
```

## Code explanation


- `import torch`: imports the PyTorch library.
- `x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`: creates a 3x3 tensor.
- `y = x.reshape(9, 1)`: reshapes the tensor to a 9x1 vector.
- `print(y)`: prints the reshaped tensor.

## Helpful links

- [PyTorch Documentation - Tensor Reshaping](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.reshape)

onelinerhub: [How can I use Python and PyTorch to reshape a tensor?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-and-pytorch-to-reshape-a-tensor)