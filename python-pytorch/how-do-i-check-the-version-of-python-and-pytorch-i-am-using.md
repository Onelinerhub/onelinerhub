# How do I check the version of Python and PyTorch I am using?
// plain

1. To check the version of Python and PyTorch you are using, you can use the `python -V` and `pip show <package name>` commands.
2. For example, to check the version of Python you are using, you can run the following code in your terminal:
```
python -V
```
This will output the version of Python you are using, e.g. `Python 3.7.3`.
3. To check the version of PyTorch you are using, you can run the following code in your terminal:
```
pip show torch
```
This will output the version of PyTorch you are using, e.g. `Name: torch
Version: 1.5.0`.
4. You can also check the version of Python and PyTorch you are using in your Python code by using the `sys` and `torch` modules.
5. For example, to check the version of Python you are using in your code, you can run the following code:
```
import sys
print(sys.version)
```
This will output the version of Python you are using, e.g. `3.7.3 (default, Apr 24 2020, 15:29:51) [MSC v.1915 64 bit (AMD64)]`.
6. To check the version of PyTorch you are using in your code, you can run the following code:
```
import torch
print(torch.__version__)
```
This will output the version of PyTorch you are using, e.g. `1.5.0`.
7. For more information on checking the version of Python and PyTorch you are using, please refer to the following links:
- [Python Documentation - sys module](https://docs.python.org/3/library/sys.html)
- [PyTorch Documentation - torch module](https://pytorch.org/docs/stable/torch.html)

onelinerhub: [How do I check the version of Python and PyTorch I am using?](https://onelinerhub.com/python-pytorch/how-do-i-check-the-version-of-python-and-pytorch-i-am-using)