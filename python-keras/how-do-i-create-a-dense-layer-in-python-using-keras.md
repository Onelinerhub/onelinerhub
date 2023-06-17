# How do I create a dense layer in Python using Keras?
// plain

In order to create a dense layer in Python using Keras, the following steps must be taken:

1. Import the necessary libraries. This includes `keras`, `tensorflow`, and `numpy`:

```
import keras
import tensorflow as tf
import numpy as np
```

2. Create a `Sequential` model:

```
model = keras.Sequential()
```

3. Add a `Dense` layer to the model. This layer will have 10 nodes and will use the `relu` activation function:

```
model.add(keras.layers.Dense(10, activation='relu'))
```

4. Compile the model using the `Adam` optimizer and `mean_squared_error` as the loss function:

```
model.compile(optimizer='Adam', loss='mean_squared_error')
```

5. Train the model using a `numpy` array of data:

```
model.fit(x_train, y_train)
```

6. Make predictions using a `numpy` array of data:

```
predictions = model.predict(x_test)
```

7. Evaluate the model using a `numpy` array of data:

```
model.evaluate(x_test, y_test)
```

## Helpful links
1. [Keras Documentation](https://keras.io/api/layers/core_layers/dense/)
2. [TensorFlow Documentation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)

onelinerhub: [How do I create a dense layer in Python using Keras?](https://onelinerhub.com/python-keras/how-do-i-create-a-dense-layer-in-python-using-keras)