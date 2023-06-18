# nano

How can I use PyTorch with Python 3.7 on a Jetson Nano?
// plain

You can use PyTorch with Python 3.7 on a Jetson Nano by following the steps below:

1. Install the required packages for PyTorch on the Jetson Nano by running the following command in the terminal:
```
$ sudo apt-get install libopenblas-base libopenmpi-dev
```

2. Install Python 3.7 on the Jetson Nano by running the command below:
```
$ sudo apt-get install python3.7
```

3. Install the PyTorch wheel file for Python 3.7 on Jetson Nano by running the command below:
```
$ wget https://nvidia.box.com/shared/static/veo87trfaawj5pfwuqvhl6mzc5b55fbj.whl -O torch-1.5.0-cp37-cp37m-linux_aarch64.whl
```

4. Install the wheel file by running the command below:
```
$ pip3 install torch-1.5.0-cp37-cp37m-linux_aarch64.whl
```

5. Verify that PyTorch is installed by running the command below:
```
$ python3
>>> import torch
>>> print(torch.__version__)
1.5.0
```

6. You can now use PyTorch with Python 3.7 on your Jetson Nano.

## Helpful links
- [Installing PyTorch on the NVIDIA Jetson Nano](https://pytorch.org/get-started/locally/#installing-pytorch-on-the-nvidia-jetson-nano)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

onelinerhub: [nano

How can I use PyTorch with Python 3.7 on a Jetson Nano?](https://onelinerhub.com/python-pytorch/nano--how-can-i-use-pytorch-with-python-----on-a-jetson-nano)