# How do I adjust the learning rate in Python Keras?
// plain

The learning rate of a neural network is a hyperparameter that controls how quickly the weights of the network are adjusted during the training process. In Python Keras, the learning rate can be adjusted by setting the `learning_rate` argument when creating the optimizer object. For example, the following code creates an optimizer with a learning rate of 0.01:

```
from keras.optimizers import SGD
opt = SGD(learning_rate=0.01)
```

In addition, the learning rate can also be adjusted during training by using a LearningRateScheduler callback. This callback can be used to reduce the learning rate over time, or to increase it if the model is not learning as expected. For example, the following code creates a LearningRateScheduler callback that reduces the learning rate by a factor of 0.1 every 5 epochs:

```
from keras.callbacks import LearningRateScheduler
def lr_scheduler(epoch):
    lr = 0.01 * 0.1**(epoch // 5)
    return lr

lr_scheduler_callback = LearningRateScheduler(lr_scheduler)
```

The parts of the code above are:

- `SGD`: This imports the Stochastic Gradient Descent optimizer from the Keras library.
- `learning_rate=0.01`: This sets the learning rate to 0.01 when creating the optimizer object.
- `lr_scheduler`: This is a function that takes an epoch as an argument and returns the learning rate for that epoch.
- `LearningRateScheduler`: This creates a callback that adjusts the learning rate based on the output of the `lr_scheduler` function.
- `epoch // 5`: This is an integer division operator that is used to calculate the number of epochs that have passed since the start of training.
- `0.1**(epoch // 5)`: This is an exponentiation operator that is used to reduce the learning rate by a factor of 0.1 every 5 epochs.

For more information, please refer to the [Keras documentation](https://keras.io/optimizers/) and the [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/LearningRateScheduler).

onelinerhub: [How do I adjust the learning rate in Python Keras?](https://onelinerhub.com/python-keras/how-do-i-adjust-the-learning-rate-in-python-keras)