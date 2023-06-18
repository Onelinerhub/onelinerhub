# How do I use Python and TensorFlow to create a Convolutional Neural Network (CNN) example?
// plain

To create a Convolutional Neural Network (CNN) example using Python and TensorFlow, the following steps can be taken:

1.  Import the necessary libraries:
```
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
```

2. Load and prepare the MNIST dataset:
```
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0
```

3. Create the convolutional base:
```
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
```

4. Add Dense layers on top:
```
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

5. Compile and train the model:
```
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)
```

6. Evaluate the model:
```
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)
```

7. Output:
```
0.9909
```

## Code Parts Explanation
- `import tensorflow as tf`: This imports the TensorFlow library into the Python environment.
- `from tensorflow.keras import datasets, layers, models`: This imports the datasets (e.g. MNIST), layers (e.g. Conv2D) and models (e.g. Sequential) modules from the Keras library.
- `(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()`: This loads the MNIST dataset into the environment.
- `train_images = train_images.reshape((60000, 28, 28, 1))`: This reshapes the training images into the shape required for the model (60000 images of 28x28 pixels with 1 channel).
- `test_images = test_images.reshape((10000, 28, 28, 1))`: This reshapes the test images into the shape required for the model (10000 images of 28x28 pixels with 1 channel).
- `train_images, test_images = train_images / 255.0, test_images / 255.0`: This normalizes the pixel values to be between 0 and 1.
- `model = models.Sequential()`: This creates a Sequential model.
- `model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))`: This adds a Conv2D layer with 32 filters of size 3x3, ReLU activation and input shape of 28x28x1.
- `model.add(layers.MaxPooling2D((2, 2)))`: This adds a MaxPooling2D layer with pool size of 2x2.
- `model.add(layers.Flatten())`: This flattens the input.
- `model.add(layers.Dense(64, activation='relu'))`: This adds a Dense layer with 64 nodes and ReLU activation.
- `model.add(layers.Dense(10, activation='softmax'))`: This adds a Dense layer with 10 nodes and Softmax activation.
- `model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])`: This compiles the model with Adam optimizer, Sparse Categorical Crossentropy loss and accuracy metric.
- `model.fit(train_images, train_labels, epochs=5)`: This fits the model on the training data for 5 epochs.
- `test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)`: This evaluates the model on the test data.
- `print(test_acc)`: This prints the accuracy of the model on the test data.

## Relevant Links
- [TensorFlow Tutorial - Convolutional Neural Network](https://www.tensorflow.org/tutorials/images/cnn)
- [Keras Tutorial - Convolutional Neural Network](https://keras.io/examples/mnist_cnn/)

onelinerhub: [How do I use Python and TensorFlow to create a Convolutional Neural Network (CNN) example?](https://onelinerhub.com/python-tensorflow/how-do-i-use-python-and-tensorflow-to-create-a-convolutional-neural-network--cnn--example)