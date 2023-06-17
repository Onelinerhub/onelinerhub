# usage

How can I check GPU usage when using Python and PyTorch?
// plain

To check GPU usage when using Python and PyTorch, you can use the `torch.cuda.memory_allocated()` function. This function returns the amount of memory currently allocated to the GPU. For example:

```
import torch

memory_allocated = torch.cuda.memory_allocated()
print(memory_allocated)
```

This will output the amount of memory allocated to the GPU in bytes.

You can also use the `torch.cuda.memory_cached()` function to check the amount of cached memory currently allocated to the GPU. For example:

```
import torch

memory_cached = torch.cuda.memory_cached()
print(memory_cached)
```

This will output the amount of cached memory allocated to the GPU in bytes.

You can also use the `torch.cuda.max_memory_allocated()` and `torch.cuda.max_memory_cached()` functions to check the maximum amount of memory allocated and cached to the GPU since the beginning of the program.

Finally, you can use the `torch.cuda.empty_cache()` function to clear the GPU memory cache.

## Code explanation


- `torch.cuda.memory_allocated()`: returns the amount of memory currently allocated to the GPU in bytes
- `torch.cuda.memory_cached()`: returns the amount of cached memory currently allocated to the GPU in bytes
- `torch.cuda.max_memory_allocated()`: returns the maximum amount of memory allocated to the GPU since the beginning of the program
- `torch.cuda.max_memory_cached()`: returns the maximum amount of cached memory allocated to the GPU since the beginning of the program
- `torch.cuda.empty_cache()`: clears the GPU memory cache

## Helpful links

- [PyTorch Documentation - CUDA Memory Management](https://pytorch.org/docs/stable/cuda.html#cuda-memory-management)

onelinerhub: [usage

How can I check GPU usage when using Python and PyTorch?](https://onelinerhub.com/python-pytorch/usage--how-can-i-check-gpu-usage-when-using-python-and-pytorch)