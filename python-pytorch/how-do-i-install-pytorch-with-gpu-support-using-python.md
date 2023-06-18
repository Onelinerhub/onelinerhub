# How do I install PyTorch with GPU support using Python?
// plain

To install PyTorch with GPU support using Python, you can follow these steps:

1. Install the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) from Nvidia, which contains the necessary libraries for GPU support.

2. Install the [cuDNN library](https://developer.nvidia.com/cudnn) from Nvidia.

3. Install the [PyTorch package](https://pytorch.org/get-started/locally/) using the pip package manager. To install with GPU support, use the following command:

```
pip install torch torchvision
```

4. To verify the installation, you can check the version of PyTorch installed using the following command:

```
python -c "import torch; print(torch.__version__)"
```

## Output example

```
1.6.0+cu101
```

5. To check if GPU support is enabled, you can use the following command:

```
python -c "import torch; print(torch.cuda.is_available())"
```

## Output example

```
True
```

6. To check the version of CUDA installed, use the following command:

```
python -c "import torch; print(torch.version.cuda)"
```

## Output example

```
10.1
```

7. To check the version of cuDNN installed, use the following command:

```
python -c "import torch; print(torch.backends.cudnn.version())"
```

## Output example

```
7603
```

onelinerhub: [How do I install PyTorch with GPU support using Python?](https://onelinerhub.com/python-pytorch/how-do-i-install-pytorch-with-gpu-support-using-python)