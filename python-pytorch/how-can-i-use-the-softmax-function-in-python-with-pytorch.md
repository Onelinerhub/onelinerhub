# How can I use the Softmax function in Python with PyTorch?
// plain

The Softmax function is a popular activation function used in many machine learning applications. It can be used in Python with PyTorch to calculate the probabilities for each class in a multi-class classification problem.

To use the Softmax function in Python with PyTorch, we can use the `torch.nn.functional.softmax` function. This function takes an input tensor of shape (N, C) and returns a tensor of shape (N, C) containing the softmax values of the input tensor.

Here is an example of how to use the `torch.nn.functional.softmax` function:

```
import torch

# Create a tensor of shape (2, 3)
input_tensor = torch.randn(2, 3)

# Calculate the softmax values of the input tensor
softmax_tensor = torch.nn.functional.softmax(input_tensor, dim=1)

print(softmax_tensor)
```

## Output example

```
tensor([[0.3096, 0.3790, 0.3114],
        [0.4536, 0.2107, 0.3357]])
```

The code above performs the following steps:
1. Import the `torch` module.
2. Create an input tensor of shape (2, 3).
3. Calculate the softmax values of the input tensor using the `torch.nn.functional.softmax` function.
4. Print the resulting softmax tensor.

For more information about the Softmax function in PyTorch, please refer to the [PyTorch documentation](https://pytorch.org/docs/stable/nn.functional.html#torch.nn.functional.softmax).

onelinerhub: [How can I use the Softmax function in Python with PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-use-the-softmax-function-in-python-with-pytorch)