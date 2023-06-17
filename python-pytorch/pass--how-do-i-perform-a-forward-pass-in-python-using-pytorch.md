# pass

How do I perform a forward pass in Python using PyTorch?
// plain

The forward pass in PyTorch can be performed by using the `forward()` method of a `nn.Module` subclass. This method takes an input `Tensor` and runs it through the model, returning the output `Tensor`.

For example, to perform a forward pass with a model `model` and input `x`, the following code can be used:
```
output = model.forward(x)
```

The `forward()` method is composed of several parts:

1. **Inputs**: The input `Tensor` is passed to the model.
2. **Layers**: The model runs the input `Tensor` through its layers, applying any necessary transformations.
3. **Output**: The output `Tensor` is then returned.

Below is a more complete example of a forward pass using a simple 3-layer model:
```
# Define model
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 2)
)

# Create input
x = torch.randn(10)

# Perform forward pass
output = model.forward(x)
```

The output of the forward pass is a `Tensor` of size `2`:
```
print(output)
# tensor([ 0.5809, -0.1188], grad_fn=<AddBackward0>)
```

For more information on performing a forward pass in PyTorch, see the [PyTorch documentation](https://pytorch.org/docs/stable/nn.html#forward).

onelinerhub: [pass

How do I perform a forward pass in Python using PyTorch?](https://onelinerhub.com/python-pytorch/pass--how-do-i-perform-a-forward-pass-in-python-using-pytorch)