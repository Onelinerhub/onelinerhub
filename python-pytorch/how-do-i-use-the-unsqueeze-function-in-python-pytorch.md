# How do I use the unsqueeze function in Python PyTorch?
// plain

The `unsqueeze` function in Python PyTorch is used to add a single-dimensional entry to a tensor. It is a function of the `torch` module and can be used to increase the dimension of a given tensor.

For example, `x = torch.tensor([1, 2, 3])` is a tensor with 3 entries. To add a single-dimensional entry to this tensor, you can use the `unsqueeze` function as follows:

```
x = torch.tensor([1,2,3])
x_unsqueezed = x.unsqueeze(0)
print(x_unsqueezed)
```

The output of the above code is `tensor([[1, 2, 3]])`.

## Code explanation

- `x = torch.tensor([1,2,3])`: This creates a tensor with 3 entries.
- `x_unsqueezed = x.unsqueeze(0)`: This adds a single-dimensional entry to the tensor `x`.
- `print(x_unsqueezed)`: This prints the tensor with the single-dimensional entry added.

Here are some ## Helpful links
- [PyTorch Documentation for Unsqueeze](https://pytorch.org/docs/stable/torch.html#torch.unsqueeze)
- [Tutorial on Unsqueeze in PyTorch](https://www.jessicayung.com/explaining-pytorch-unsqueeze-and-squeeze/)

onelinerhub: [How do I use the unsqueeze function in Python PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-use-the-unsqueeze-function-in-python-pytorch)