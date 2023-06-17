# How can I enable CUDA support in Python PyTorch?
// plain

To enable CUDA support in Python PyTorch, you need to have an Nvidia GPU with CUDA installed. To check if your GPU has CUDA enabled, you can run the following code:

```
import torch
print(torch.cuda.is_available())
```

If the output is `True`, then CUDA is enabled.

To enable CUDA support in PyTorch, you need to install the appropriate version of PyTorch with CUDA support. This can be done by running the following command:

```
pip install torch===1.7.0+cu110 torchvision===0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```

This command will install PyTorch version 1.7.0 with CUDA 11.0 support.

Once PyTorch is installed, you can check if CUDA is enabled by running the following code:

```
import torch
print(torch.cuda.is_available())
```

If the output is `True`, then CUDA is enabled and you are ready to use PyTorch with CUDA support.

## Code explanation


1. `import torch`: imports the PyTorch library
2. `print(torch.cuda.is_available())`: checks if CUDA is enabled
3. `pip install torch===1.7.0+cu110 torchvision===0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html`: installs the appropriate version of PyTorch with CUDA support

## Helpful links

1. [PyTorch with CUDA support](https://pytorch.org/get-started/locally/)
2. [Checking if CUDA is enabled](https://pytorch.org/docs/stable/cuda.html#checking-if-cuda-is-available)

onelinerhub: [How can I enable CUDA support in Python PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-enable-cuda-support-in-python-pytorch)