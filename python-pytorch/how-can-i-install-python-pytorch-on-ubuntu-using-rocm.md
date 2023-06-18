# How can I install Python PyTorch on Ubuntu using ROCm?
// plain

1. First, make sure that your system meets the prerequisites for building and running PyTorch on ROCm. You will need to have the following installed:

- Ubuntu 18.04 or higher
- ROCm 3.5 or higher
- Python 3.6 or higher
- GCC 7.4 or higher

2. After you have the prerequisites installed, you can install PyTorch on ROCm using the following command:

```
pip3 install torch-rocm
```

3. After the installation is complete, you can verify that the installation was successful by running the following command:

```
python3 -c "import torch; print(torch.__version__)"
```

## Output example


```
1.7.0a0+f6b1b8d
```

4. To use PyTorch with ROCm, you can use the following command:

```
python3 -m torch.utils.collect_env
```

5. This will display the environment variables that PyTorch needs to use ROCm. You can also check the version of PyTorch that is installed by running the following command:

```
python3 -c "import torch; print(torch.version.cuda)"
```

## Output example


```
9.2
```

6. To use PyTorch with ROCm, you will need to set the environment variable `HIP_VISIBLE_DEVICES` to the GPU device ID. This can be done by running the following command:

```
export HIP_VISIBLE_DEVICES=0
```

7. You can now use PyTorch with ROCm by running the following command:

```
python3 -m torch.utils.collect_env
```

## Helpful links

- [PyTorch ROCm Installation Guide](https://pytorch.org/rocm/)
- [ROCm Documentation](https://rocm.github.io/ROCmDocs/)

onelinerhub: [How can I install Python PyTorch on Ubuntu using ROCm?](https://onelinerhub.com/python-pytorch/how-can-i-install-python-pytorch-on-ubuntu-using-rocm)