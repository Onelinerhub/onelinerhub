# How do I convert a list to a tensor in Python PyTorch?
// plain

To convert a list to a tensor in Python PyTorch, you can use the `torch.tensor()` function. For example:

```
import torch

list_data = [1, 2, 3]
tensor_data = torch.tensor(list_data)
print(tensor_data)

# Output: tensor([1, 2, 3])
```

In this example code, the following parts are used:

- `import torch`: This imports the `torch` module, which provides the `torch.tensor()` function.

- `list_data = [1, 2, 3]`: This creates a list of numbers that will be converted to a tensor.

- `tensor_data = torch.tensor(list_data)`: This uses the `torch.tensor()` function to convert the list to a tensor.

- `print(tensor_data)`: This prints the tensor to the console.

For more information, please see the [PyTorch documentation](https://pytorch.org/docs/stable/tensors.html).

onelinerhub: [How do I convert a list to a tensor in Python PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-convert-a-list-to-a-tensor-in-python-pytorch)