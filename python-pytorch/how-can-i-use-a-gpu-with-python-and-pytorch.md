# How can I use a GPU with Python and PyTorch?
// plain

The easiest way to use a GPU with Python and PyTorch is to install the PyTorch library. PyTorch is a deep learning library that provides access to GPU computing. To use a GPU with PyTorch, you will need to install the GPU version of PyTorch.

Once PyTorch is installed, you can use it to create a deep learning model and train it on a GPU. To do this, you will need to specify the device type when creating the model. For example, the following code will create a model on the GPU:

```
import torch
model = torch.nn.Sequential(
    torch.nn.Linear(input_dim, hidden_dim),
    torch.nn.ReLU(),
    torch.nn.Linear(hidden_dim, output_dim),
    device="cuda"
)
```

You can then train the model on the GPU by specifying the device type when calling the `model.fit()` method. For example:

```
model.fit(X_train, y_train, device="cuda")
```

You can also use PyTorch to perform other GPU-accelerated operations such as matrix multiplication and convolution. To do this, you can use the `torch.cuda` module. For example, the following code will perform a matrix multiplication on the GPU:

```
import torch.cuda
A = torch.randn(1000, 1000).cuda()
B = torch.randn(1000, 1000).cuda()
C = torch.matmul(A, B)
```

## Helpful links

- [PyTorch Documentation](https://pytorch.org/docs/stable/)
- [PyTorch GPU Support](https://pytorch.org/docs/stable/notes/cuda.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

onelinerhub: [How can I use a GPU with Python and PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-use-a-gpu-with-python-and-pytorch)