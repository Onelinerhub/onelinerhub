# How do I create a neural network using Python and Keras?
// plain

Creating a neural network using Python and Keras is a relatively straightforward process.

First, we need to import the necessary libraries:
```
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
```

Next, we need to define the model. In this example, we will use a sequential model with two layers:
```
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
```

The first line creates a sequential model, which is a linear stack of layers. The second line adds a densely connected layer with 12 neurons and an input dimension of 8. The third line adds a densely connected layer with 8 neurons.

Finally, we need to compile and fit the model:
```
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=150, batch_size=10)
```

The first line compiles the model using the categorical crossentropy loss function, the adam optimizer, and accuracy as a metric. The second line fits the model to the data (X and Y) using 150 epochs and a batch size of 10.

## Helpful links
- [Keras Documentation](https://keras.io/)
- [Keras Sequential Model Guide](https://keras.io/getting-started/sequential-model-guide/)
- [Keras Layers Guide](https://keras.io/layers/core/)
- [Keras Compilation Guide](https://keras.io/getting-started/sequential-model-guide/#compilation)
- [Keras Fitting Guide](https://keras.io/getting-started/sequential-model-guide/#fitting-the-model)

onelinerhub: [How do I create a neural network using Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-create-a-neural-network-using-python-and-keras)