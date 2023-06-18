# How can I resolve the error "cannot import name 'get_config' from 'tensorflow.python.eager.context'"?
// plain

The error "cannot import name 'get_config' from 'tensorflow.python.eager.context'" indicates that the version of TensorFlow installed is too low. To resolve this error, you should upgrade your TensorFlow version to the latest version.

For example, if you are using pip to install TensorFlow, you can use the following command to upgrade to the latest version:

```
pip install --upgrade tensorflow
```

You can also use the following command to check the version of your installed TensorFlow:

```
pip show tensorflow
```

The output should look something like this:

```
Name: tensorflow
Version: 2.3.1
```

Once you have updated your TensorFlow version, you should be able to import the `get_config` module.

## Code explanation


1. `pip install --upgrade tensorflow`: Upgrades TensorFlow to the latest version.
2. `pip show tensorflow`: Checks the version of your installed TensorFlow.

## Helpful links

- [TensorFlow Installation Guide](https://www.tensorflow.org/install)

onelinerhub: [How can I resolve the error "cannot import name 'get_config' from 'tensorflow.python.eager.context'"?](https://onelinerhub.com/python-tensorflow/how-can-i-resolve-the-error--cannot-import-name--get-config--from--tensorflow-python-eager-context-)