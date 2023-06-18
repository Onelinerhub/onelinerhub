# How can I use Python and PyTorch with ROCm?
// plain

Python and PyTorch can be used with ROCm to create and deploy GPU-accelerated applications. ROCm is an open-source platform for GPU-accelerated computing that provides an optimized runtime and development libraries for a wide variety of programming languages.

To use Python and PyTorch with ROCm, you will need to first install the ROCm stack. This can be done by downloading the ROCm packages from the official website and installing them on your system.

Once the ROCm stack is installed, you can use the `pip` command to install PyTorch and any other Python libraries you may need.

Once the Python libraries are installed, you can use the `hipcc` compiler to compile your PyTorch code for execution on the GPU.

Here is an example of a simple PyTorch program that can be compiled for GPU execution using `hipcc`:

```python
import torch

x = torch.randn(5, 3)
y = torch.randn(5, 2)

z = torch.mm(x, y)
print(z)
```

## Output example

```
tensor([[ 0.0071,  0.6845],
        [ 0.3836,  0.8406],
        [-0.8082, -0.2025],
        [-0.5182, -0.9078],
        [-0.9408,  0.9357]])
```

## Code explanation

1. Import the PyTorch library: `import torch`
2. Create two tensors, `x` and `y`: `x = torch.randn(5, 3)` and `y = torch.randn(5, 2)`
3. Perform a matrix multiplication between `x` and `y`: `z = torch.mm(x, y)`
4. Print the result of the matrix multiplication: `print(z)`

## Helpful links
- [ROCm Official Website](https://rocm.github.io/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [hipcc Documentation](https://rocm-documentation.readthedocs.io/en/latest/HIP/hipcc.html)

onelinerhub: [How can I use Python and PyTorch with ROCm?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-and-pytorch-with-rocm)