# How can I use Python and TensorFlow to create a stock prediction model?
// plain

Using Python and TensorFlow to create a stock prediction model is a popular machine learning task. The following is an example of how to do this:

```
#import TensorFlow and other libraries
import tensorflow as tf
import numpy as np

#define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

#compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

#provide the data
xs = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float)
ys = np.array([1.5,3,4.5,6,7.5,9,10.5,12,13.5,15], dtype=float)

#train the model
model.fit(xs, ys, epochs=500)

#make a prediction
print(model.predict([11.0]))
```
## Output example

```
[[16.492437]]
```

## Code explanation


1. Import TensorFlow and other libraries: `import tensorflow as tf` and `import numpy as np`
2. Define the model: `model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])`
3. Compile the model: `model.compile(optimizer='sgd', loss='mean_squared_error')`
4. Provide the data: `xs = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float)` and `ys = np.array([1.5,3,4.5,6,7.5,9,10.5,12,13.5,15], dtype=float)`
5. Train the model: `model.fit(xs, ys, epochs=500)`
6. Make a prediction: `print(model.predict([11.0]))`

## Helpful links

- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras)
- [Creating a Stock Prediction Model with Python and TensorFlow](https://www.edureka.co/blog/stock-prediction-model-python-tensorflow/)

onelinerhub: [How can I use Python and TensorFlow to create a stock prediction model?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-and-tensorflow-to-create-a-stock-prediction-model)