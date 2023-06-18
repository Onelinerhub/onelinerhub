# How do I use PyTorch with Python 3.9?
// plain

PyTorch is a powerful open source deep learning framework that can be used with Python 3.9. To use PyTorch, you need to install the PyTorch package for Python 3.9. This can be done with the following command:

```
pip install torch
```

Once PyTorch is installed, you can import it into your Python code and start using it. For example, you can create a basic tensor using the following code:

```
import torch
x = torch.tensor([1,2,3])
print(x)
```

## Output example

```
tensor([1, 2, 3])
```

The code above imports the PyTorch package, creates a tensor with the values 1, 2, and 3, and prints the tensor.

You can also use PyTorch to create and train neural networks. For example, you can create a basic neural network using the following code:

```
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(in_features=2, out_features=4)
        self.fc2 = nn.Linear(in_features=4, out_features=2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x

net = Net()
```

The code above imports the PyTorch package and the torch.nn module, creates a neural network class with two linear layers, and instantiates the neural network.

For more information on using PyTorch with Python 3.9, please refer to the [PyTorch Documentation](https://pytorch.org/docs/stable/index.html).

*[PyTorch](https://pytorch.org/), [Python 3.9](https://www.python.org/downloads/release/python-390/)*

onelinerhub: [How do I use PyTorch with Python 3.9?](https://onelinerhub.com/python-pytorch/how-do-i-use-pytorch-with-python-----1687051073)