# How can I install PyTorch using Pip on Python?
// plain

PyTorch can be installed using Pip on Python with the following steps:

1. Install Python 3.6 or higher:
```
python --version
```
## Output example
 `Python 3.7.3`

2. Install Pip:
```
python -m pip install --upgrade pip
```

3. Install PyTorch:
```
python -m pip install torch torchvision
```

4. Check whether PyTorch is installed properly:
```
python -c "import torch; print(torch.__version__)"
```
## Output example
 `1.4.0`

5. Install a specific version of PyTorch:
```
python -m pip install torch==1.3.1 torchvision==0.4.2
```

6. Install PyTorch with GPU support:
```
python -m pip install torch torchvision
```

7. Install PyTorch with CUDA support:
```
python -m pip install torch torchvision -f https://download.pytorch.org/whl/torch_stable.html
```

## Helpful links
- [PyTorch Official Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)

onelinerhub: [How can I install PyTorch using Pip on Python?](https://onelinerhub.com/python-pytorch/how-can-i-install-pytorch-using-pip-on-python)