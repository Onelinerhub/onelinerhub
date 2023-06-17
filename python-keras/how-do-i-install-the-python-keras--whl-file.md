# How do I install the Python Keras .whl file?
// plain

1. Download the .whl file from the [Keras website](https://keras.io/#installation).
2. Open the command prompt and navigate to the directory where the .whl file is located.
3. Install Keras by running the command `pip install <filename>.whl`

   ```
   pip install keras-2.3.1-cp37-cp37m-win_amd64.whl
   ```

   Output:
   ```
   Processing c:\users\user\downloads\keras-2.3.1-cp37-cp37m-win_amd64.whl
   Installing collected packages: keras
   Successfully installed keras-2.3.1
   ```
4. Verify the installation by running the command `pip show keras`

   ```
   pip show keras
   ```

   Output:
   ```
   Name: Keras
   Version: 2.3.1
   Summary: Deep Learning for humans
   Home-page: https://keras.io
   Author: Francois Chollet
   Author-email: francois.chollet@gmail.com
   License: MIT
   Location: c:\users\user\anaconda3\lib\site-packages
   Requires: numpy, scipy, pyyaml, h5py
   Required-by:
   ```
5. Start using Keras by importing it in your Python code:

   ```python
   import keras
   ```
6. To check the version of Keras, run the command `keras.__version__`

   ```python
   keras.__version__
   ```

   Output:
   ```
   '2.3.1'
   ```
7. For more information, refer to the [Keras documentation](https://keras.io/).

onelinerhub: [How do I install the Python Keras .whl file?](https://onelinerhub.com/python-keras/how-do-i-install-the-python-keras--whl-file)