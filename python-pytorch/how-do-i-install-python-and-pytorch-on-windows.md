# How do I install Python and PyTorch on Windows?
// plain

1. Download and install the latest version of Python 3 from the [Python website](https://www.python.org/downloads/).
2. Open the command prompt and type `pip install torch` to install PyTorch.
3. To check the installation, type `python` in the command prompt and you should see something like this:
```
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
4. Type `import torch` and you should see something like this:
```
>>> import torch
>>>
```
5. To check the version of PyTorch, type `print(torch.__version__)` and you should see something like this:
```
>>> print(torch.__version__)
1.2.0
>>>
```
6. To check the available packages in PyTorch, type `print(torch.utils.package_dir)` and you should see something like this:
```
>>> print(torch.utils.package_dir)
C:\Users\USERNAME\AppData\Local\Programs\Python\Python37\lib\site-packages\torch
>>>
```
7. You have successfully installed Python and PyTorch on Windows.

## Helpful links
- [Python website](https://www.python.org/downloads/)
- [PyTorch website](https://pytorch.org/)

onelinerhub: [How do I install Python and PyTorch on Windows?](https://onelinerhub.com/python-pytorch/how-do-i-install-python-and-pytorch-on-windows)