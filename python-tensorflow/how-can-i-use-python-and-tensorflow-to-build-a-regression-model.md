# How can I use Python and TensorFlow to build a regression model?
// plain

To build a regression model using Python and TensorFlow, you will need to import the TensorFlow library, define the input data, define the model, and then compile and fit the model.

```
import tensorflow as tf

# define input data
X = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = tf.constant([[1], [3], [5], [7], [9]])

# define model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_dim=2))

# compile and fit model
model.compile(loss='mean_squared_error', optimizer='sgd')
model.fit(X, y, epochs=50)
```

## Output example


```
Epoch 1/50
1/1 [==============================] - 0s 2ms/step - loss: 0.0014
Epoch 2/50
1/1 [==============================] - 0s 2ms/step - loss: 0.0014
...
Epoch 49/50
1/1 [==============================] - 0s 2ms/step - loss: 5.9087e-05
Epoch 50/50
1/1 [==============================] - 0s 2ms/step - loss: 5.5274e-05
```

## Code explanation

1. Importing the TensorFlow library: `import tensorflow as tf`
2. Defining the input data: `X = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])` and `y = tf.constant([[1], [3], [5], [7], [9]])`
3. Defining the model: `model = tf.keras.Sequential()` and `model.add(tf.keras.layers.Dense(units=1, input_dim=2))`
4. Compiling and fitting the model: `model.compile(loss='mean_squared_error', optimizer='sgd')` and `model.fit(X, y, epochs=50)`

## Helpful links
- [TensorFlow Regression Tutorial](https://www.tensorflow.org/tutorials/keras/regression)
- [TensorFlow Getting Started Guide](https://www.tensorflow.org/guide/keras/overview)

onelinerhub: [How can I use Python and TensorFlow to build a regression model?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-and-tensorflow-to-build-a-regression-model)