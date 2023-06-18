# How do I download a Python Scipy .whl file?
// plain

1. Download the appropriate version of the Python Scipy .whl file from the [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy) website.
2. Make sure to choose the correct version for your version of Python (e.g. Python 3.6).
3. Open the command prompt or terminal and navigate to the folder where the .whl file is located.
4. Run the command `pip install <filename>.whl` where `<filename>` is the name of the .whl file.
5. If you have multiple versions of Python installed, you can specify the version of Python you want to install the package for by running the command `pip3 install <filename>.whl` (for Python 3).
6. The package will be installed and you should get a confirmation message.
7. You can check if the package was installed correctly by running the command `python -c "import scipy"` in the command prompt or terminal.

Example code block:
```
pip install scipy-1.2.0-cp36-cp36m-win_amd64.whl
```
Example output:
```
Processing c:\users\user\downloads\scipy-1.2.0-cp36-cp36m-win_amd64.whl
Installing collected packages: scipy
Successfully installed scipy-1.2.0
```

onelinerhub: [How do I download a Python Scipy .whl file?](https://onelinerhub.com/python-scipy/how-do-i-download-a-python-scipy--whl-file)