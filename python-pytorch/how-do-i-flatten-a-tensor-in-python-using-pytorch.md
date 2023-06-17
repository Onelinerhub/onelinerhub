# How do I flatten a tensor in Python using PyTorch?
// plain

To flatten a tensor in Python using PyTorch, you can use the `.view()` method. This method reshapes a tensor into a different size without changing its data.

For example:
```
import torch

x = torch.randn(2,3,4)

y = x.view(-1)

print(y)
```
## Output example

```
tensor([ 0.1772, -0.0717,  0.0362, -1.0058, -0.3590, -0.3914,  0.7644,  0.9333,
        -0.3182,  1.0144,  1.9072,  0.5056])
```

The code above creates a tensor with shape (2,3,4) and then reshapes it into a tensor with shape (12,) using the `.view()` method.

The `.view()` method takes in two parameters:
- `-1` which means that the size of the dimension should be inferred from the size of the tensor.
- `size` which is a tuple that specifies the desired shape of the tensor.

For more information on the `.view()` method, please refer to the [PyTorch Documentation](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.view).

onelinerhub: [How do I flatten a tensor in Python using PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-flatten-a-tensor-in-python-using-pytorch)