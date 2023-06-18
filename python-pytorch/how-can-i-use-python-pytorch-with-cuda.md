# How can I use Python PyTorch with CUDA?
// plain

PyTorch is a popular deep learning library that can be used with CUDA to accelerate computations. To use PyTorch with CUDA, one must have a CUDA-enabled GPU and the appropriate version of PyTorch installed.

## Example code

```
import torch
torch.cuda.is_available()
```

## Output example

```
True
```

The code above checks whether CUDA is available on the system. If it returns `True`, then CUDA is available and can be used with PyTorch.

To use CUDA with PyTorch, one must also specify the device to be used for computations. This is done by setting the `device` to either `"cuda"` or `"cpu"` in the code.

## Example code

```
import torch
device = torch.device("cuda")
```

This code sets the device to be used for computations to `cuda`.

Finally, one must also ensure that the CUDA-enabled GPU is correctly detected by PyTorch. This is done by setting the `CUDA_VISIBLE_DEVICES` environment variable to the index of the GPU to be used.

## Example code

```
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
```

In the example above, the environment variable is set to `0`, which means the first CUDA-enabled GPU on the system will be used.

Once these steps are completed, PyTorch can be used with CUDA to accelerate computations.

## Helpful links
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch CUDA Support](https://pytorch.org/docs/stable/notes/cuda.html)

onelinerhub: [How can I use Python PyTorch with CUDA?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-pytorch-with-cuda)