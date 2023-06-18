# How do I use a Python TensorFlow Keras model to make predictions?
// plain

Using a Python TensorFlow Keras model to make predictions involves the following steps:

1. Load the model:

```
from keras.models import load_model
model = load_model('model.h5')
```

2. Prepare the input data:

```
import numpy as np
x_test = np.array([[1,2,3]])
```

3. Make predictions:

```
prediction = model.predict(x_test)
print(prediction)
# [[0.1, 0.2, 0.7]]
```

The model will output an array of probabilities, representing the likelihood of each possible outcome.

For more information, please refer to the [Keras documentation](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model) and the [TensorFlow documentation](https://www.tensorflow.org/guide/keras/overview).

onelinerhub: [How do I use a Python TensorFlow Keras model to make predictions?](https://onelinerhub.com/python-tensorflow/how-do-i-use-a-python-tensorflow-keras-model-to-make-predictions)