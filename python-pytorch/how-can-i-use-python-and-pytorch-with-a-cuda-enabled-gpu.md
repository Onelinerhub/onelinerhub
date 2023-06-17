# How can I use Python and PyTorch with a CUDA-enabled GPU?
// plain

To use Python and PyTorch with a CUDA-enabled GPU, you need to install the CUDA Toolkit and the PyTorch library. After installation, you can use Python and PyTorch to create and run programs on the GPU.

To demonstrate, here is an example of a simple program that adds two numbers on the GPU:

```
import torch

# Create two random tensors on the GPU
a = torch.randn(3, device="cuda")
b = torch.randn(3, device="cuda")

# Add the two tensors on the GPU
c = a + b

# Print the result
print(c)
```

## Output example

```
tensor([-1.6619,  0.0403,  0.9107], device='cuda:0')
```

The code consists of the following parts:

1. Import the torch library: `import torch`
2. Create two random tensors on the GPU: `a = torch.randn(3, device="cuda")` and `b = torch.randn(3, device="cuda")`
3. Add the two tensors on the GPU: `c = a + b`
4. Print the result: `print(c)`

For more information, see the [PyTorch Documentation](https://pytorch.org/docs/stable/index.html) and [CUDA Documentation](https://docs.nvidia.com/cuda/).

onelinerhub: [How can I use Python and PyTorch with a CUDA-enabled GPU?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-and-pytorch-with-a-cuda-enabled-gpu)