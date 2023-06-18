# How do I install Python Pytorch?
// plain

1. First, you will need to install Python on your machine. You can find instructions for doing so [here](https://www.python.org/downloads/).

2. Once you have Python installed, you can install PyTorch using `pip`. For example, you can use the following command:
```
pip install torch torchvision
```

3. After PyTorch has been installed, you can verify that it is working correctly by running the following code:
```
import torch
print(torch.__version__)
```
This will print out the version of PyTorch that you have installed.

4. If you would like to use PyTorch with a specific version of Python, you can specify the Python version when installing PyTorch. For example, if you are using Python 3.7, you can use the following command:
```
pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

5. If you are using a GPU, you will need to install the CUDA Toolkit before installing PyTorch. You can find instructions for doing so [here](https://developer.nvidia.com/cuda-downloads).

6. After CUDA has been installed, you can install PyTorch with GPU support by using the following command:
```
pip install torch torchvision
```

7. Finally, you can verify that PyTorch is working correctly with GPU support by running the following code:
```
import torch
print(torch.cuda.is_available())
```
This will print out `True` if GPU support is available, or `False` if it is not.

onelinerhub: [How do I install Python Pytorch?](https://onelinerhub.com/python-pytorch/how-do-i-install-python-pytorch)