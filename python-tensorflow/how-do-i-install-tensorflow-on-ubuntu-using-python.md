# How do I install Tensorflow on Ubuntu using Python?
// plain

Installing Tensorflow on Ubuntu with Python is relatively straightforward.

1. First, you will need to install the Python package manager, `pip`. You can do this by running the following command in your terminal:

```
sudo apt-get install python-pip
```

2. Next, you will need to install the `virtualenv` package, which will allow you to create a virtual environment in which you can install Tensorflow. To do this, you will need to run the following command:

```
pip install virtualenv
```

3. Once the `virtualenv` package is installed, you can create a virtual environment by running the following command:

```
virtualenv --system-site-packages -p python3 ~/venv_tf
```

4. Now that the virtual environment has been created, you can activate it by running the following command:

```
source ~/venv_tf/bin/activate
```

5. You can now install Tensorflow into the virtual environment by running the following command:

```
pip install --upgrade tensorflow
```

6. Finally, you can verify that Tensorflow has been installed correctly by running the following command:

```
python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

The output of this command should be a random number.

## Helpful links

- [Installing Tensorflow](https://www.tensorflow.org/install)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

onelinerhub: [How do I install Tensorflow on Ubuntu using Python?](https://onelinerhub.com/python-tensorflow/how-do-i-install-tensorflow-on-ubuntu-using-python)