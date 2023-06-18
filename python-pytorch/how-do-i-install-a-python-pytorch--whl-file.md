# How do I install a Python PyTorch .whl file?
// plain

1. Download the appropriate .whl file for your system from the [PyTorch website](https://pytorch.org/get-started/locally/).
2. Open a command prompt/terminal and navigate to the directory containing the .whl file.
3. Run the command `pip install <filename>.whl`, where `<filename>` is the name of the file you downloaded.
4. If the installation is successful, you will see the following output:
```
Successfully installed torch-1.7.0+cu101
```
5. To check that the installation was successful, you can run the command `python -c "import torch; print(torch.__version__)"`.
6. If the installation was successful, the output should be the version number of PyTorch you installed:
```
1.7.0+cu101
```
7. You can now use PyTorch in your Python programs.

onelinerhub: [How do I install a Python PyTorch .whl file?](https://onelinerhub.com/python-pytorch/how-do-i-install-a-python-pytorch--whl-file)