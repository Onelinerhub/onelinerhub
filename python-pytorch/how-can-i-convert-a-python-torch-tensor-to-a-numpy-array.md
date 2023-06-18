# How can I convert a Python Torch tensor to a Numpy array?
// plain

To convert a Python Torch tensor to a Numpy array, the `numpy()` function can be used. It takes in a tensor as a parameter and returns a Numpy array.

## Example code

```
import torch
import numpy as np

tensor = torch.randn(2,3)
numpy_array = tensor.numpy()

print(tensor)
print(numpy_array)
```
Example output:
```
tensor([[ 0.9016,  0.2183, -0.2770],
        [-0.6709,  0.9398, -1.1486]])

[[ 0.9016  0.2183 -0.277 ]
 [-0.6709  0.9398 -1.1486]]
```

The `numpy()` function is part of the Torch tensor class, and it can be used to convert a Torch tensor to a Numpy array. The code above shows an example of using the `numpy()` function to convert a Torch tensor to a Numpy array.

## Helpful links

- [PyTorch Documentation: Tensor Class](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)
- [PyTorch Documentation: Tensor to NumPy](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.numpy)

onelinerhub: [How can I convert a Python Torch tensor to a Numpy array?](https://onelinerhub.com/python-pytorch/how-can-i-convert-a-python-torch-tensor-to-a-numpy-array)