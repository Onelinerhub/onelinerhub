# How can I use the @ operator in Python with PyTorch?
// plain

The @ operator is a shorthand notation for the [`torch.matmul`](https://pytorch.org/docs/stable/torch.html#torch.matmul) function in PyTorch. It performs matrix multiplication of two tensors and returns the result as a single tensor.

To use the @ operator in Python with PyTorch, we need to first create two tensors. For example:

```
import torch

tensor_a = torch.tensor([[1,2], [3,4]])
tensor_b = torch.tensor([[5,6], [7,8]])
```

Then, we can use the @ operator to perform matrix multiplication between the two tensors:

```
matmul_result = tensor_a @ tensor_b

print(matmul_result)
```

## Output example

```
tensor([[19, 22],
        [43, 50]])
```

The @ operator is equivalent to the following code:

```
matmul_result = torch.matmul(tensor_a, tensor_b)

print(matmul_result)
```

The output will be the same.

The @ operator is a convenient shorthand notation for the `torch.matmul` function in PyTorch. It can be used to perform matrix multiplication of two tensors and returns the result as a single tensor.

onelinerhub: [How can I use the @ operator in Python with PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-use-the---operator-in-python-with-pytorch)