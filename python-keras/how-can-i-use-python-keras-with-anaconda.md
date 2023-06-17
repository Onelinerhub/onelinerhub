# How can I use Python Keras with Anaconda?
// plain

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. Anaconda is a data science platform that comes with a lot of useful tools for data science development.

Using Keras with Anaconda is quite simple. To install Keras, you can use the `conda install` command in the Anaconda Prompt:

```
conda install -c conda-forge keras
```

Once Keras is installed, you can import it in your Python scripts and use it to build your neural networks. For example, you can use the `Sequential` model to define a simple neural network:

```
from keras.models import Sequential
model = Sequential()
```

You can then add layers to the model, such as a `Dense` layer with a `relu` activation function:

```
from keras.layers import Dense
model.add(Dense(64, activation='relu'))
```

Finally, you can compile the model and fit it to your data:

```
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train,
          batch_size=32, epochs=10)
```

In summary, using Keras with Anaconda is a simple process:

1. Use the `conda install` command to install Keras.
2. Import Keras in your Python scripts.
3. Use the `Sequential` model to define your neural network.
4. Add layers to the model.
5. Compile and fit the model to your data.

## Helpful links

- Keras: https://keras.io/
- Anaconda: https://www.anaconda.com/

onelinerhub: [How can I use Python Keras with Anaconda?](https://onelinerhub.com/python-keras/how-can-i-use-python-keras-with-anaconda)