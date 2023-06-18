# How do I install PyTorch with CUDA using Python?
// plain

1. First, you need to install PyTorch with CUDA support. This can be done with the following command:
```
pip install torch torchvision
```

2. After installation, you need to check if PyTorch is installed with CUDA support. This can be done with the following command:
```
python -c "import torch; print(torch.cuda.is_available())"
```

The output of this command should be `True` if PyTorch is installed with CUDA support.

3. After installation, you need to set up the environment variables for CUDA. This can be done with the following command:
```
export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

4. You then need to check if the environment variables are set correctly. This can be done with the following command:
```
echo $PATH
echo $LD_LIBRARY_PATH
```

The output of these commands should include the paths that were set in step 3.

5. Finally, you need to check if PyTorch is using the correct CUDA version. This can be done with the following command:
```
python -c "import torch; print(torch.version.cuda)"
```

The output of this command should be the version of CUDA that you installed in step 1.

**## Helpful links**
- https://pytorch.org/
- https://pytorch.org/get-started/locally/
- https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

onelinerhub: [How do I install PyTorch with CUDA using Python?](https://onelinerhub.com/python-pytorch/how-do-i-install-pytorch-with-cuda-using-python)