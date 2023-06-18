# How do I install Python PyTorch on Ubuntu?
// plain

1. First, install the Python PyTorch package from the PyTorch website. You can use the following command:
   ```
   pip install torch
   ```
2. Next, install PyTorch's dependencies using the following command:
   ```
   sudo apt-get install libopenblas-dev liblapack-dev
   ```
3. After that, install the GPU version of PyTorch using the following command:
   ```
   pip install torch torchvision
   ```
4. Once the installation is complete, you can verify the installation by running the following command:
   ```
   python -c "import torch; print(torch.__version__)"
   ```
   Output:
   ```
   1.6.0+cu101
   ```
5. You can also check the list of available packages for PyTorch using the following command:
   ```
   pip list | grep torch
   ```
   Output:
   ```
   torch               1.6.0+cu101
   torchvision         0.7.0+cu101
   ```
6. To get started with PyTorch, you can refer to the official documentation [here](https://pytorch.org/docs/stable/index.html).
7. You can also refer to the official tutorials [here](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html).

onelinerhub: [How do I install Python PyTorch on Ubuntu?](https://onelinerhub.com/python-pytorch/how-do-i-install-python-pytorch-on-ubuntu)