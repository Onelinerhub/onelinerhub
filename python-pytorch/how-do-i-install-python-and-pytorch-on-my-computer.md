# How do I install Python and PyTorch on my computer?
// plain

1. Download and install the latest version of Python from [Python.org](https://www.python.org/).
2. Install the PyTorch library using `pip install torch` in the command line.
3. Verify the installation by running the following code:
```
import torch
print(torch.__version__)
```
4. The output should be the version of PyTorch installed, for example:
```
1.6.0
```
5. To install a specific version of PyTorch, run `pip install torch==<version>`, replacing `<version>` with the desired version.
6. To install the GPU version of PyTorch, run `pip install torch===<version>+cu101`, replacing `<version>` with the desired version and `cu101` with the version of CUDA installed on your system.
7. To learn more about installation, visit the [PyTorch documentation](https://pytorch.org/docs/stable/index.html).

onelinerhub: [How do I install Python and PyTorch on my computer?](https://onelinerhub.com/python-pytorch/how-do-i-install-python-and-pytorch-on-my-computer)