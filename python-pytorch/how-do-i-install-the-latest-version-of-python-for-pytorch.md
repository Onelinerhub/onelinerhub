# How do I install the latest version of Python for PyTorch?
// plain

1. To install the latest version of Python for PyTorch, you need to first install [Python 3.6 or later](https://www.python.org/downloads/).
2. Once Python is installed, you can install PyTorch using `pip` with the following command:
```
pip install torch
```
3. To check if the installation was successful, you can run the following command:
```
python -c "import torch; print(torch.__version__)"
```
## Output example
 `1.7.0`
4. You can also install PyTorch from source. To do that, you need to download the latest version of PyTorch from the [PyTorch website](https://pytorch.org/get-started/locally/) and follow the instructions provided there.
5. If you are using Anaconda, you can also install PyTorch from the Anaconda Cloud with the following command:
```
conda install pytorch torchvision -c pytorch
```
6. If you are using Windows, you can also install PyTorch with the [Microsoft Visual Studio IDE](https://docs.microsoft.com/en-us/visualstudio/python/installing-python-support-in-visual-studio?view=vs-2019).
7. For more detailed instructions, you can refer to the [PyTorch installation guide](https://pytorch.org/get-started/locally/).

onelinerhub: [How do I install the latest version of Python for PyTorch?](https://onelinerhub.com/python-pytorch/how-do-i-install-the-latest-version-of-python-for-pytorch)