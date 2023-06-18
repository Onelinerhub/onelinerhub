# How do I save a PyTorch tensor to a file using Python?
// plain

To save a PyTorch tensor to a file using Python, use the following steps:

1. Import the necessary libraries:
```python
import torch
import numpy as np
```

2. Create a tensor object:
```python
x = torch.tensor([1, 2, 3])
```

3. Save the tensor to a file:
```python
torch.save(x, 'x_tensor.pt')
```

4. Verify that the tensor has been saved correctly by loading it back into memory:
```python
x2 = torch.load('x_tensor.pt')
print(x2)
```
## Output example

```
tensor([1, 2, 3])
```

5. Save the tensor as a numpy array:
```python
np.save('x_tensor.npy', x.numpy())
```

6. Verify that the numpy array has been saved correctly by loading it back into memory:
```python
x3 = np.load('x_tensor.npy')
print(x3)
```
## Output example

```
[1 2 3]
```

7. Finally, you can also save the tensor to a text file:
```python
torch.save(x, open('x_tensor.txt', 'w'))
```

## Helpful links
- [PyTorch Documentation - torch.save](https://pytorch.org/docs/stable/torch.html#torch.save)
- [PyTorch Documentation - torch.load](https://pytorch.org/docs/stable/torch.html#torch.load)
- [Numpy Documentation - np.save](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
- [Numpy Documentation - np.load](https://numpy.org/doc/stable/reference/generated/numpy.load.html)

onelinerhub: [How do I save a PyTorch tensor to a file using Python?](https://onelinerhub.com/python-pytorch/how-do-i-save-a-pytorch-tensor-to-a-file-using-python)