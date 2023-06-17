# How do I export a PyTorch model to ONNX?
// plain

1. PyTorch models can be exported to ONNX using the torch.onnx.export() function.
2. This function takes in a PyTorch model, a list of input tensors, and an output file name as arguments.
```
# Example
import torch
import torch.onnx

# Create a model
model = torch.nn.Linear(1, 1)

# Create an input tensor
x = torch.randn(1, 1)

# Export the model
torch.onnx.export(model, x, "model.onnx")
```
3. This will create a model.onnx file containing the ONNX representation of the model.
4. The function also takes an optional set of parameters to specify the operator set version and other optimization options.
5. The torch.onnx.export() function is part of the torch.onnx package.
6. For more information, see the [PyTorch ONNX documentation](https://pytorch.org/docs/stable/onnx.html).
7. For a full example of exporting a model to ONNX, see the [PyTorch ONNX tutorial](https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html).

onelinerhub: [How do I export a PyTorch model to ONNX?](https://onelinerhub.com/python-pytorch/how-do-i-export-a-pytorch-model-to-onnx)