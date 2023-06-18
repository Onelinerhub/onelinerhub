# How can I use Python PyTorch without CUDA?
// plain

You can use Python PyTorch without CUDA by setting the `device` to `cpu` when creating the Tensors. For example:

```
import torch

x = torch.rand(5, 3)
print(x.device)

device = torch.device("cpu")
x = torch.rand(5, 3, device=device)
print(x.device)
```

## Output example

```
cpu
cpu
```

1. `import torch` imports the PyTorch library.
2. `x = torch.rand(5, 3)` creates a tensor of size (5, 3) on the default device, which is usually the GPU.
3. `print(x.device)` prints the device on which the tensor is located.
4. `device = torch.device("cpu")` creates a CPU device object.
5. `x = torch.rand(5, 3, device=device)` creates a tensor of size (5, 3) on the CPU device.
6. `print(x.device)` prints the device on which the tensor is located.

## Helpful links
- https://pytorch.org/docs/stable/tensors.html
- https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py

onelinerhub: [How can I use Python PyTorch without CUDA?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-pytorch-without-cuda)