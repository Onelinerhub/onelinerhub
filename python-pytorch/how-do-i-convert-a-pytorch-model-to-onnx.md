# How do I convert a PyTorch model to ONNX?
// plain

Converting a PyTorch model to ONNX is a straightforward process. Below is an example code block of how to do this:

```
import torch
import torch.onnx

# Create a model
model = torch.nn.Linear(1, 1)

# Create a fake input
x = torch.randn(1, 1)

# Export the model
torch.onnx.export(model, x, "model.onnx")
```

This code will create a file called "model.onnx" which contains the converted model.

The code consists of several parts:
1. Importing the torch and torch.onnx modules
2. Creating the model
3. Creating a fake input
4. Exporting the model

For more information, please refer to the official PyTorch documentation on [exporting a model to ONNX](https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html).

onelinerhub: [How do I convert a PyTorch model to ONNX?](https://onelinerhub.com/python-pytorch/how-do-i-convert-a-pytorch-model-to-onnx)