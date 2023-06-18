# How can I use Python Poetry to install PyTorch?
// plain

Python Poetry is a tool used to manage dependencies and create virtual environments for Python projects. It can be used to install PyTorch, a popular open-source deep learning library for Python.

To install PyTorch with Python Poetry, first create a new project directory and `cd` into it:

```
$ mkdir my_pytorch_project
$ cd my_pytorch_project
```

Then, create a `pyproject.toml` file to define the dependencies for the project. This file should include the following lines to install PyTorch:

```
[tool.poetry.dependencies]
python = "^3.7"
pytorch = "^1.6.0"
```

Next, run `poetry install` to install the dependencies. This will create a virtual environment for the project and install PyTorch in it.

```
$ poetry install
Creating virtualenv my_pytorch_project in /Users/username/.cache/pypoetry/virtualenvs
Installing dependencies from lock file

Package operations: 7 installs, 0 updates, 0 removals
  - Installing numpy (1.19.2)
  - Installing torch (1.6.0)
  - Installing torchvision (0.7.0)
  - Installing six (1.15.0)
  - Installing future (0.18.2)
  - Installing typing-extensions (3.7.4.3)
  - Installing wheel (0.35.1)
```

Finally, activate the virtual environment and check that PyTorch is installed:

```
$ poetry shell
$ python
>>> import torch
>>> torch.__version__
'1.6.0'
```

## Code explanation

- `mkdir my_pytorch_project`: create a new project directory
- `cd my_pytorch_project`: change working directory to the new project directory
- `[tool.poetry.dependencies]`: define the dependencies in the `pyproject.toml` file
- `python = "^3.7"`: install Python version 3.7 or higher
- `pytorch = "^1.6.0"`: install PyTorch version 1.6.0 or higher
- `poetry install`: install the dependencies and create a virtual environment
- `poetry shell`: activate the virtual environment
- `import torch`: import the PyTorch library
- `torch.__version__`: check the version of PyTorch installed

## Helpful links
- https://python-poetry.org/docs/
- https://pytorch.org/

onelinerhub: [How can I use Python Poetry to install PyTorch?](https://onelinerhub.com/python-pytorch/how-can-i-use-python-poetry-to-install-pytorch)