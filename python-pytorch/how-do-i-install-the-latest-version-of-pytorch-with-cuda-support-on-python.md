# How do I install the latest version of PyTorch with CUDA support on Python?
// plain

1. First, you need to install the latest version of PyTorch with CUDA support for Python. To do this, you can use the pip command:
```
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```
2. After the installation is complete, you can check the version of PyTorch and CUDA you have installed by running the following command:
```
python -c "import torch; print(torch.__version__)"
```
The output should be something like `1.6.0+cu101`.
3. Once you have verified the version of PyTorch and CUDA you have installed, you can check if CUDA is enabled by running the following command:
```
python -c "import torch; print(torch.cuda.is_available())"
```
If the output is `True`, then CUDA is enabled.
4. You can also check the version of CUDA you have installed by running the following command:
```
nvcc --version
```
5. Finally, you can check the GPU you have installed by running the following command:
```
nvidia-smi
```

- Pip command: `pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html`
- Check PyTorch version: `python -c "import torch; print(torch.__version__)"`
- Check CUDA enabled: `python -c "import torch; print(torch.cuda.is_available())"`
- Check CUDA version: `nvcc --version`
- Check GPU installed: `nvidia-smi`

## Helpful links
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [CUDA Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

onelinerhub: [How do I install the latest version of PyTorch with CUDA support on Python?](https://onelinerhub.com/python-pytorch/how-do-i-install-the-latest-version-of-pytorch-with-cuda-support-on-python)