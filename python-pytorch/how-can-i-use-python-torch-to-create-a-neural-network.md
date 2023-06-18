# How can I use Python Torch to create a neural network?
// plain

Using Python Torch to create a neural network is easy and straightforward. To get started, first install the torch library with `pip install torch`.

Once installed, you can create a neural network with just a few lines of code. For example, the following code creates a neural network with two layers, each with 5 neurons:

```
import torch

# Create a neural network with two layers, each with 5 neurons
model = torch.nn.Sequential(
    torch.nn.Linear(5, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 5)
)

print(model)
```

## Output example


```
Sequential(
  (0): Linear(in_features=5, out_features=5, bias=True)
  (1): ReLU()
  (2): Linear(in_features=5, out_features=5, bias=True)
)
```

The code consists of the following parts:

- `import torch`: Imports the torch library.
- `model = torch.nn.Sequential(...)`: Creates a neural network with two layers, each with 5 neurons.
- `torch.nn.Linear(5, 5)`: Creates a linear layer with 5 input and 5 output neurons.
- `torch.nn.ReLU()`: Creates a ReLU activation layer.
- `print(model)`: Prints the model structure.

For more information on creating neural networks with Python Torch, see the [PyTorch Neural Networks tutorial](https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html).

onelinerhub: [How can I use Python Torch to create a neural network?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-torch-to-create-a-neural-network)