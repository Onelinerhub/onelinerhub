# How can I convert a Python PyTorch tensor to a NumPy array?
// plain

To convert a Python PyTorch tensor to a NumPy array, you can use the PyTorch `.numpy()` method. This method will return the tensor as a NumPy array.

## Example


```
import torch
x = torch.tensor([1, 2, 3])
y = x.numpy()
print(y)
```

## Output example

```
[1 2 3]
```

The code above consists of the following parts:

1. `import torch` imports the PyTorch library.
2. `x = torch.tensor([1, 2, 3])` creates a PyTorch tensor with values 1, 2, and 3.
3. `y = x.numpy()` converts the PyTorch tensor to a NumPy array.
4. `print(y)` prints the NumPy array.

## Helpful links
- [PyTorch Documentation - Tensor](https://pytorch.org/docs/stable/tensors.html)
- [NumPy Documentation - Array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

onelinerhub: [How can I convert a Python PyTorch tensor to a NumPy array?](https://onelinerhub.com/python-pytorch/how-can-i-convert-a-python-pytorch-tensor-to-a-numpy-array)