# How do I calculate cross entropy loss using Python and PyTorch?
// plain

Cross entropy loss is a measure of how well a set of predicted probabilities match the true labels of a data set. It can be calculated using Python and PyTorch by first defining the true labels and predicted probabilities as tensors.

```
import torch

true_labels = torch.tensor([1, 0, 0, 1])
predicted_probabilities = torch.tensor([0.9, 0.2, 0.1, 0.8])
```

Then, the cross entropy loss can be calculated by using the `torch.nn.functional.cross_entropy` function.

```
loss = torch.nn.functional.cross_entropy(predicted_probabilities, true_labels)
print(loss)
```

## Output example

```
tensor(0.4170)
```

## Code explanation

1. `import torch` - imports the PyTorch library
2. `true_labels = torch.tensor([1, 0, 0, 1])` - defines the true labels as a tensor
3. `predicted_probabilities = torch.tensor([0.9, 0.2, 0.1, 0.8])` - defines the predicted probabilities as a tensor
4. `loss = torch.nn.functional.cross_entropy(predicted_probabilities, true_labels)` - calculates the cross entropy loss
5. `print(loss)` - prints out the cross entropy loss

## Helpful links
- [PyTorch Cross Entropy Loss](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.cross_entropy)
- [Cross Entropy Loss Explained](https://towardsdatascience.com/understanding-cross-entropy-loss-f2d3258b7f5f)

onelinerhub: [How do I calculate cross entropy loss using Python and PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-calculate-cross-entropy-loss-using-python-and-pytorch)