# How do I access the value of a tensor in PyTorch?
// plain

To access the value of a tensor in PyTorch, you can call the `.item()` method on the tensor object. This method will return the value of the tensor as a Python object.

For example,

```
import torch
x = torch.tensor([[1, 2], [3, 4]])
print(x.item())
```

## Output example

```
1
```

The `.item()` method works for scalar tensors, i.e., tensors with only one element. If the tensor has multiple elements, then you can use the `.numpy()` method to convert the tensor to a NumPy array and then access the elements using array indexing.

For example,

```
import torch
x = torch.tensor([[1, 2], [3, 4]])
print(x.numpy()[1,1])
```

## Output example

```
4
```

You can also use the `.tolist()` method to convert the tensor to a Python list and then access the elements using list indexing.

For example,

```
import torch
x = torch.tensor([[1, 2], [3, 4]])
print(x.tolist()[1][1])
```

## Output example

```
4
```

For more information, see the [PyTorch documentation](https://pytorch.org/docs/stable/tensors.html#accessing-elements).

onelinerhub: [How do I access the value of a tensor in PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-access-the-value-of-a-tensor-in-pytorch)