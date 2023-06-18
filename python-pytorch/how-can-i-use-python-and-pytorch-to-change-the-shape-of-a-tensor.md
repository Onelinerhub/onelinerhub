# How can I use Python and PyTorch to change the shape of a tensor?
// plain

To change the shape of a tensor using Python and PyTorch, you can use the `.view` method. This method will return a new tensor with the same data as the original tensor but with a different shape.

## Example code

```
import torch

tensor = torch.randn(2,3)
print("Original shape:", tensor.shape)

tensor_reshaped = tensor.view(3,2)
print("Reshaped shape:", tensor_reshaped.shape)
```

## Output example

```
Original shape: torch.Size([2, 3])
Reshaped shape: torch.Size([3, 2])
```

## Code explanation

1. `import torch`: imports the PyTorch library.
2. `torch.randn(2,3)`: creates a tensor with shape (2,3).
3. `tensor.view(3,2)`: returns a tensor with the same data as the original tensor but with shape (3,2).

## Helpful links
- [PyTorch Documentation: Tensor](https://pytorch.org/docs/stable/tensors.html)
- [PyTorch Documentation: Tensor Reshaping](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.view)

onelinerhub: [How can I use Python and PyTorch to change the shape of a tensor?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-and-pytorch-to-change-the-shape-of-a-tensor)