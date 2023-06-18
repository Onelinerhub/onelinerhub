# How do I install PyTorch using pip?
// plain

Installing PyTorch using pip is a simple process. Here are the steps to follow:

1. Make sure your system has pip installed. If it doesn't, you can install it with `python -m pip install --upgrade pip`

2. Select the correct command for your system. For Linux, it is `pip3 install torch torchvision`. For Windows, it is `pip install torch===1.6.0 torchvision===0.7.0`

3. Execute the command.

```
$ pip3 install torch torchvision
Collecting torch
  Downloading https://files.pythonhosted.org/packages/30/57/d5cceb0799c06733eefce80c395459f28970ebb9e896846ce96ab579a3f1/torch-1.6.0-cp36-cp36m-manylinux1_x86_64.whl (748.0MB)
Collecting torchvision
  Downloading https://files.pythonhosted.org/packages/9a/0e/6c7d8c37212d4f9d5f6cae4f3b7b8fc5d6b7f2b89b2b3b4b46e5f7d8a8e2/torchvision-0.7.0-cp36-cp36m-manylinux1_x86_64.whl (6.2MB)
Installing collected packages: torch, torchvision
Successfully installed torch-1.6.0 torchvision-0.7.0
```

4. Verify the installation by importing the library in Python.

```
$ python
>>> import torch
>>> print(torch.__version__)
1.6.0
```

5. You can also check the version of PyTorch installed by running `pip freeze` command.

```
$ pip freeze
torch==1.6.0
torchvision==0.7.0
```

That's it. You have successfully installed PyTorch using pip.

## Helpful links
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Install PyTorch](https://pytorch.org/get-started/locally/)

onelinerhub: [How do I install PyTorch using pip?](https://onelinerhub.com/python-pytorch/how-do-i-install-pytorch-using-pip)