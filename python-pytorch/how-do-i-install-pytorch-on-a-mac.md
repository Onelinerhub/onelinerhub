# How do I install PyTorch on a Mac?
// plain

1. Prerequisites:
    - Python 3.6 or later
    - macOS 10.14 or later
    - Xcode 11.3 or later

2. Install PyTorch:
    - Open a terminal window and run the following command:
    ```
    pip3 install torch torchvision
    ```

3. Confirm installation:
    - To confirm that PyTorch is installed correctly, run the following command:
    ```
    python3 -c "import torch; print(torch.__version__)"
    ```
    - Output: `1.7.1`

4. Install required dependencies:
    - Install additional dependencies, such as cffi and numpy, with the following command:
    ```
    pip3 install cffi numpy
    ```

5. Install additional packages:
    - Install additional packages, such as Jupyter Notebook and Matplotlib, with the following command:
    ```
    pip3 install jupyter matplotlib
    ```

6. Verify installation:
    - To verify that the installation is correct, run the following command:
    ```
    python3 -c "import torch; import jupyter; import matplotlib"
    ```
    - If there are no errors, the installation is successful.

7. Further information:
    - For further information, please refer to the [PyTorch installation guide](https://pytorch.org/get-started/locally/).

onelinerhub: [How do I install PyTorch on a Mac?](https://onelinerhub.com/python-pytorch/how-do-i-install-pytorch-on-a-mac)