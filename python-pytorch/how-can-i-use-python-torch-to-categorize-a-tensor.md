# How can I use Python Torch to categorize a tensor?
// plain

To categorize a tensor with Python Torch, you can use the torch.max() function. This function takes a tensor and returns the maximum value of each row in the tensor. The output is a tensor with the same shape as the input tensor, but with each row containing the maximum value of that row.

## Example

```
import torch

x = torch.tensor([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(torch.max(x, dim=1))
```
## Output example

```
tensor([3, 6, 9])
```

The torch.max() function takes two parameters:

* `x` is the tensor we are categorizing.
* `dim` is the dimension along which we are calculating the maximum values. In this case, `dim=1` means that we want to calculate the maximum value of each row.

## Helpful links
* [PyTorch Documentation - torch.max()](https://pytorch.org/docs/stable/torch.html#torch.max)

onelinerhub: [How can I use Python Torch to categorize a tensor?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-torch-to-categorize-a-tensor)