# How can I use a Long Short-Term Memory (LSTM) network in Python with PyTorch?
// plain

To use a Long Short-Term Memory (LSTM) network in Python with PyTorch, you need to import the necessary packages and define the network architecture.

```
import torch
import torch.nn as nn

class LSTMNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super(LSTMNetwork, self).__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim

        # Define the LSTM layer
        self.lstm = nn.LSTM(input_dim, hidden_dim, layer_dim, batch_first=True)

        # Define the output layer
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()

        # Initialize cell state
        c0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()

        # One time step
        out, (hn, cn) = self.lstm(x, (h0, c0))

        # Index hidden state of last time step
        # out.size() --> 100, 28, 100
        # out[:, -1, :] --> 100, 100 --> just want last time step hidden states!
        out = self.fc(out[:, -1, :])
        # out.size() --> 100, 10
        return out

input_dim = 28
hidden_dim = 100
layer_dim = 2
output_dim = 10

model = LSTMNetwork(input_dim, hidden_dim, layer_dim, output_dim)
```

The code above defines the architecture of an LSTM network with two layers, a hidden dimension of 100, and an output dimension of 10. The forward method performs one time step of the LSTM and returns the output of the last time step.

## Code explanation

1. `import torch` and `import torch.nn as nn`: Import the necessary packages.
2. `class LSTMNetwork(nn.Module):`: Define the network architecture as a class.
3. `self.lstm = nn.LSTM(input_dim, hidden_dim, layer_dim, batch_first=True)`: Define the LSTM layer.
4. `self.fc = nn.Linear(hidden_dim, output_dim)`: Define the output layer.
5. `h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()` and `c0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()`: Initialize the hidden state and cell state.
6. `out, (hn, cn) = self.lstm(x, (h0, c0))`: Perform one time step of the LSTM.
7. `out = self.fc(out[:, -1, :])`: Index the hidden state of the last time step.

## Helpful links
- [PyTorch LSTM tutorial](https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html#sphx-glr-beginner-nlp-sequence-models-tutorial-py)
- [PyTorch LSTM documentation](https://pytorch.org/docs/stable/nn.html#lstm)

onelinerhub: [How can I use a Long Short-Term Memory (LSTM) network in Python with PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-use-a-long-short-term-memory--lstm--network-in-python-with-pytorch)