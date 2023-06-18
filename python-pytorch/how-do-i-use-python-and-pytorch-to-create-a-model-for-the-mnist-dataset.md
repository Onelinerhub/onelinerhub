# How do I use Python and PyTorch to create a model for the MNIST dataset?
// plain

To create a model for the MNIST dataset using Python and PyTorch, you will need to:

1. Import the necessary PyTorch modules and other Python libraries:
```
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
```

2. Load the MNIST dataset:
```
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1307,), (0.3081,))
                   ])),
    batch_size=64, shuffle=True)
```

3. Define the model architecture:
```
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
```

4. Instantiate the model and define the loss function and optimizer:
```
model = Net()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
```

5. Train the model:
```
for epoch in range(10):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
```

6. Evaluate the model:
```
test_loss = 0
correct = 0
for data, target in test_loader:
    output = model(data)
    test_loss += F.nll_loss(output, target, size_average=False).item() # sum up batch loss
    pred = output.data.max(1, keepdim=True)[1] # get the index of the max log-probability
    correct += pred.eq(target.data.view_as(pred)).cpu().sum()

test_loss /= len(test_loader.dataset)
print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
    test_loss, correct, len(test_loader.dataset),
    100. * correct / len(test_loader.dataset)))
```

7. Output:
```
Test set: Average loss: 0.0445, Accuracy: 9876/10000 (99%)
```

## Helpful links
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

onelinerhub: [How do I use Python and PyTorch to create a model for the MNIST dataset?](https://onelinerhub.com/python-pytorch/how-do-i-use-python-and-pytorch-to-create-a-model-for-the-mnist-dataset)