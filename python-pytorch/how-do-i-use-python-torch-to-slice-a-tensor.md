# How do I use Python torch to slice a tensor?
// plain

To slice a tensor using Python torch, you can use the `torch.index_select()` function. This function takes three arguments: the tensor to be sliced, the dimension along which to slice, and the indices of the elements to be selected. For example:

```
import torch

tensor = torch.rand(4, 3)

# Slice along dim 0, selecting indices 0 and 2
sliced_tensor = torch.index_select(tensor, 0, torch.LongTensor([0, 2]))

print(sliced_tensor)
```

## Output example

```
tensor([[0.5404, 0.7369, 0.0682],
        [0.0338, 0.1420, 0.3483]])
```

The code above will select the first and third elements along dimension 0 of the tensor `tensor`.

The code consists of the following parts:

1. `import torch`: Imports the `torch` library.
2. `tensor = torch.rand(4, 3)`: Creates a tensor with shape (4, 3).
3. `torch.index_select(tensor, 0, torch.LongTensor([0, 2]))`: Uses the `torch.index_select()` function to slice along dimension 0 of `tensor`, selecting the elements with indices 0 and 2.
4. `print(sliced_tensor)`: Prints the resulting tensor.

## Helpful links

- [Python Documentation: torch.index_select()](https://pytorch.org/docs/stable/torch.html#torch.index_select)

onelinerhub: [How do I use Python torch to slice a tensor?](https://onelinerhub.com/python-pytorch/how-do-i-use-python-torch-to-slice-a-tensor)