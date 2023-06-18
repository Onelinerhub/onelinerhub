# How do I use nn.linear in Python Pytorch?
// plain

`nn.linear` is a module in Pytorch that allows you to create a linear layer in a neural network. To use it, you need to first import the module:
```
import torch.nn as nn
```

You can then create a linear layer with the following code:
```
linear = nn.Linear(in_features, out_features)
```
Where `in_features` is the number of input features, and `out_features` is the number of output features.

You can also specify the bias of the linear layer:
```
linear = nn.Linear(in_features, out_features, bias=True)
```

You can then use the `linear` layer in your neural network. For example, if you have a neural network with two linear layers, you can define it as:
```
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = nn.Linear(3, 4)
        self.linear2 = nn.Linear(4, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.linear2(x)
        return x

net = Net()
```

You can then pass an input `x` of shape `(batch_size, 3)` through the neural network:
```
x = torch.randn(2, 3)
out = net(x)
print(out)
```
This will output:
```
tensor([[-0.7137],
        [-0.8232]], grad_fn=<AddmmBackward>)
```

#### Code parts and Explanation
- `import torch.nn as nn`: imports the `nn` module from `torch.nn`
- `nn.Linear(in_features, out_features)`: creates a linear layer with the given `in_features` and `out_features`
- `nn.Linear(in_features, out_features, bias=True)`: creates a linear layer with the given `in_features` and `out_features` and sets the bias to `True`
- `class Net(nn.Module):`: defines a new neural network class `Net` that inherits from `nn.Module`
- `self.linear1 = nn.Linear(3, 4)`: creates a linear layer with 3 input features and 4 output features
- `self.linear2 = nn.Linear(4, 1)`: creates a linear layer with 4 input features and 1 output feature
- `def forward(self, x):`: defines the forward pass of the neural network
- `x = self.linear1(x)`: passes the input `x` through the first linear layer
- `x = self.linear2(x)`: passes the output of the first linear layer through the second linear layer
- `net = Net()`: creates an instance of the neural network
- `x = torch.randn(2, 3)`: creates a random input `x` of shape `(2, 3)`
- `out = net(x)`: passes the input `x` through the neural network
- `print(out)`: prints the output of the neural network

#### Relevant Links
- [PyTorch Documentation - nn.Linear](https://pytorch.org/docs/stable/nn.html#linear)

onelinerhub: [How do I use nn.linear in Python Pytorch?](https://onelinerhub.com/python-pytorch/how-do-i-use-nn-linear-in-python-pytorch)