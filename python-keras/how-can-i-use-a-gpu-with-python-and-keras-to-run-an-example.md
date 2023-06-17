# How can I use a GPU with Python and Keras to run an example?
// plain

Using a GPU with Python and Keras to run an example is quite simple.

1. First, you must install the necessary packages:

```
pip install tensorflow-gpu
pip install keras
```

2. Then, you must set the backend to use the GPU:

```
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
```

3. Finally, you can run your example code:

```
import tensorflow as tf
from keras.models import Sequential

model = Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
```

## Output example

```
[[18.979214]]
```

The code above will use the GPU to run an example of training a simple linear model using Keras and TensorFlow.

The first two lines install the necessary packages. The third line sets the backend to use the GPU. The fourth line imports the necessary libraries. The fifth line creates a model and adds a single layer. The sixth line compiles the model. The seventh and eighth lines create the data. The ninth line trains the model. The tenth line prints the prediction for the given input.

## Helpful links
- [TensorFlow GPU Installation Guide](https://www.tensorflow.org/install/gpu)
- [Keras Installation Guide](https://keras.io/#installation)

onelinerhub: [How can I use a GPU with Python and Keras to run an example?](https://onelinerhub.com/python-keras/how-can-i-use-a-gpu-with-python-and-keras-to-run-an-example)