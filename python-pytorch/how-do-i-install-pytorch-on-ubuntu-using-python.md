# How do I install PyTorch on Ubuntu using Python?
// plain

1. Install the latest version of Python3 using `sudo apt install python3`
2. Install PyTorch using `pip3 install torch torchvision`
3. Verify the installation by running the following code block:
```
import torch
print(torch.__version__)
```
## Output example
 `1.5.1`
4. Install Jupyter Notebook using `pip3 install jupyter`
5. Verify the installation by running the following code block:
```
import jupyter
print(jupyter.__version__)
```
## Output example
 `1.0.0`
6. Create a virtual environment using `virtualenv -p python3 venv`
7. Activate the virtual environment using `source venv/bin/activate`

## Helpful links
- [Install Python on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04)
- [Install PyTorch](https://pytorch.org/get-started/locally/)
- [Install Jupyter Notebook](https://jupyter.org/install)
- [Create Virtual Environment](https://docs.python.org/3/tutorial/venv.html)

onelinerhub: [How do I install PyTorch on Ubuntu using Python?](https://onelinerhub.com/python-pytorch/how-do-i-install-pytorch-on-ubuntu-using-python)