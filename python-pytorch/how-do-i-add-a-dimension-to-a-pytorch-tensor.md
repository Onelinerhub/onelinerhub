# How do I add a dimension to a PyTorch tensor?
// plain

Adding a dimension to a PyTorch tensor is done using the `unsqueeze()` method. This method adds a single-dimensional entry to the tensor at a given position. For example:

```
import torch

x = torch.tensor([1, 2, 3])

# Add a dimension at position 0
y = x.unsqueeze(0)

print(y)
```

## Output example

```
tensor([[1, 2, 3]])
```

The code above creates a new tensor `y` with an additional dimension at position 0.

The `unsqueeze()` method takes one argument, the position of the new dimension. This argument is optional; if no argument is provided, the new dimension will be added at the end.

## Code explanation

- `import torch`: imports the PyTorch library into the current environment
- `x = torch.tensor([1, 2, 3])`: creates a PyTorch tensor with the values 1, 2, and 3
- `y = x.unsqueeze(0)`: adds a single-dimensional entry to the tensor `x` at position 0, and assigns the result to the tensor `y`
- `print(y)`: prints the tensor `y`

## Helpful links
- [PyTorch Documentation: Tensor](https://pytorch.org/docs/stable/tensors.html)
- [PyTorch Documentation: Tensor.unsqueeze()](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.unsqueeze)

onelinerhub: [How do I add a dimension to a PyTorch tensor?](https://onelinerhub.com/python-pytorch/how-do-i-add-a-dimension-to-a-pytorch-tensor)