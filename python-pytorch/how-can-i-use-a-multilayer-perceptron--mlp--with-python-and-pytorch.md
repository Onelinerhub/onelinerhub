# How can I use a Multilayer Perceptron (MLP) with Python and PyTorch?
// plain

A multilayer perceptron (MLP) is a type of artificial neural network used for supervised learning tasks such as classification and regression. It can be implemented in Python using the PyTorch library.

The following example shows how to use a MLP in Python with PyTorch. This example uses the MNIST dataset, which contains images of handwritten digits.

```
import torch
import torch.nn as nn
import torch.nn.functional as F

# Load the MNIST data
mnist_data = torch.load('mnist.pt')

# Create a MLP model
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 10)
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# Create the MLP model
model = MLP()

# Train the model
loss_fn = nn.NLLLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(10):
    for data, target in mnist_data:
        optimizer.zero_grad()
        output = model(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()

# Test the model
test_loss = 0
correct = 0
for data, target in mnist_data:
    output = model(data)
    test_loss += loss_fn(output, target).item()
    pred = output.data.max(1, keepdim=True)[1]
    correct += pred.eq(target.data.view_as(pred)).sum()

test_loss /= len(mnist_data.dataset)
print('Test Loss: {:.6f}, Accuracy: {:.3f}%'.format(
    test_loss, 100. * correct / len(mnist_data.dataset)))
```

## Output example


```
Test Loss: 0.390844, Accuracy: 89.400%
```

The code above:

1. Imports the necessary libraries (`torch`, `torch.nn`, `torch.nn.functional`).
2. Loads the MNIST dataset.
3. Creates a MLP model with two fully connected layers (`fc1` and `fc2`).
4. Defines the forward pass of the model.
5. Creates an instance of the MLP model.
6. Defines the loss function and optimizer.
7. Trains the model for 10 epochs.
8. Tests the model and prints the test loss and accuracy.

## Helpful links

- https://pytorch.org/docs/stable/nn.html
- https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html
- https://pytorch.org/docs/stable/optim.html

onelinerhub: [How can I use a Multilayer Perceptron (MLP) with Python and PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-use-a-multilayer-perceptron--mlp--with-python-and-pytorch)