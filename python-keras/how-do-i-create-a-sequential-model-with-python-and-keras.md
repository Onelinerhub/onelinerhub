# How do I create a sequential model with Python and Keras?
// plain

Creating a sequential model with Python and Keras is an easy task. A sequential model is a linear stack of layers.

To create a sequential model with Python and Keras, you need to import the `Sequential` class from Keras. Then you can add layers to the model by calling the `add()` method.

```
from keras.models import Sequential

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
```

The above code creates a sequential model with two layers. The first layer has 32 neurons, an `relu` activation function, and an input dimension of 100. The second layer has 1 neuron and a `sigmoid` activation function.

Once you have constructed the model, you need to compile it with an appropriate loss function and optimizer.

```
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

The above code compiles the model with an `rmsprop` optimizer, a `binary_crossentropy` loss function, and an `accuracy` metric.

Finally, you can then train the model with the `fit()` method.

```
model.fit(data, labels, epochs=10, batch_size=32)
```

The above code trains the model for 10 epochs with a batch size of 32.

## Helpful links

- [Keras Documentation - Sequential Model](https://keras.io/getting-started/sequential-model-guide/)
- [Keras Documentation - Compiling a Model](https://keras.io/getting-started/sequential-model-guide/#compilation)
- [Keras Documentation - Training a Model](https://keras.io/getting-started/sequential-model-guide/#training)

onelinerhub: [How do I create a sequential model with Python and Keras?](https://onelinerhub.com/python-keras/how-do-i-create-a-sequential-model-with-python-and-keras)