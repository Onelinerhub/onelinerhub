# How do I install PyTorch on a Windows computer?
// plain

1. Install the [PyTorch pre-compiled binary wheel](https://pytorch.org/get-started/locally/) according to your system configuration, e.g. for **CPU-only** Windows 10 and Python 3.7:

```
pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

2. Verify the installation by running a small test program such as:

```
import torch
x = torch.rand(5, 3)
print(x)
```

## Output example

```
tensor([[0.3236, 0.9200, 0.8447],
        [0.9221, 0.7366, 0.3277],
        [0.1781, 0.9082, 0.4459],
        [0.5090, 0.9583, 0.4251],
        [0.7274, 0.9019, 0.6324]])
```

3. If you have a **GPU**, you can install the GPU version of PyTorch, e.g. for CUDA 10.1 and Python 3.7:

```
pip install torch===1.4.0+cu101 torchvision===0.5.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

4. After installation, you can check if your GPU is detected by PyTorch by running the following code:

```
import torch
print(torch.cuda.is_available())
```

## Output example

```
True
```

5. To ensure that PyTorch is using the GPU, you can run the following code:

```
import torch
x = torch.rand(5, 3)
print(x)
if torch.cuda.is_available():
  device = torch.device("cuda")
  y = torch.ones_like(x, device=device)
  x = x.to(device)
  z = x + y
  print(z)
```

## Output example

```
tensor([[0.7717, 0.9653, 0.8269],
        [0.7152, 0.8271, 0.5182],
        [0.9807, 0.2540, 0.7920],
        [0.7888, 0.1350, 0.6153],
        [0.0356, 0.7261, 0.9131]])
tensor([[1.7717, 1.9653, 1.8269],
        [1.7152, 1.8271, 1.5182],
        [1.9807, 1.2540, 1.7920],
        [1.7888, 1.1350, 1.6153],
        [1.0356, 1.7261, 1.9131]], device='cuda:0')
```

6. To learn more about installing PyTorch on Windows, please refer to the official [documentation](https://pytorch.org/get-started/locally/).

7. For more detailed instructions on how to install PyTorch, please refer to the [tutorials](https://pytorch.org/tutorials/).

onelinerhub: [How do I install PyTorch on a Windows computer?](https://onelinerhub.com/python-pytorch/how-do-i-install-pytorch-on-a-windows-computer)