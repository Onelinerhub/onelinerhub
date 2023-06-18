# How do I convert a torch tensor to a numpy array in Python?
// plain

To convert a torch tensor to a numpy array in Python, you can use the `.numpy()` method. This method converts a torch tensor to a numpy array.

## Example

```
import torch

x = torch.tensor([1, 2, 3])

# convert tensor to numpy array
y = x.numpy()

print(y)
```
## Output example

```
[1 2 3]
```

The code above consists of the following parts:
1. `import torch`: This imports the `torch` library into the program
2. `x = torch.tensor([1, 2, 3])`: This creates a torch tensor with the values `1`, `2`, and `3`
3. `y = x.numpy()`: This converts the torch tensor `x` to a numpy array and stores it in the variable `y`
4. `print(y)`: This prints the numpy array stored in the variable `y`

## Helpful links
- [PyTorch Docs - Tensor](https://pytorch.org/docs/stable/tensors.html)
- [PyTorch Docs - Converting to NumPy](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.numpy)

onelinerhub: [How do I convert a torch tensor to a numpy array in Python?](https://onelinerhub.com/python-pytorch/how-do-i-convert-a-torch-tensor-to-a-numpy-array-in-python)