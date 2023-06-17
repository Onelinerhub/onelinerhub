# How can I use the Python Keras Applications library to build a neural network?
// plain

Keras Applications is a library of pre-trained models with deep learning algorithms, developed with a high-level API for building and training models. It can be used to build a neural network in Python.

## Example code


```
from keras.applications import MobileNet

# Create the base model of MobileNet
model = MobileNet(weights='imagenet', include_top=False)

# Add a new top layer
x = model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(512, activation='relu')(x)
preds = Dense(2, activation='softmax')(x)

# Create a new model
model_2 = Model(inputs=model.input, outputs=preds)

# Freeze the layers
for layer in model_2.layers[:20]:
    layer.trainable=False
for layer in model_2.layers[20:]:
    layer.trainable=True

# Compile the model
model_2.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

This code creates a new model based on MobileNet, adds a new top layer, freezes layers, and compiles the model.

## Code explanation

1. `from keras.applications import MobileNet`: imports the MobileNet model from the Keras Applications library.
2. `model = MobileNet(weights='imagenet', include_top=False)`: creates the base model of MobileNet using the pre-trained weights from ImageNet and excluding the top layer.
3. `x = model.output`: creates a new output layer.
4. `x = GlobalAveragePooling2D()(x)`: applies global average pooling to the output layer.
5. `x = Dense(1024, activation='relu')(x)`: adds a dense layer with 1024 neurons and ReLU activation.
6. `x = Dense(1024, activation='relu')(x)`: adds a dense layer with 1024 neurons and ReLU activation.
7. `x = Dense(512, activation='relu')(x)`: adds a dense layer with 512 neurons and ReLU activation.
8. `preds = Dense(2, activation='softmax')(x)`: adds a dense layer with 2 neurons and softmax activation.
9. `model_2 = Model(inputs=model.input, outputs=preds)`: creates a new model with the inputs from the original model and the new output layer.
10. `for layer in model_2.layers[:20]:`: freezes the first 20 layers of the model.
11. `for layer in model_2.layers[20:]:`: allows the remaining layers to be trained.
12. `model_2.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])`: compiles the model with the Adam optimizer, categorical cross entropy loss function, and accuracy metric.

## Helpful links
- [Keras Applications Documentation](https://keras.io/api/applications/)
- [MobileNet Documentation](https://keras.io/api/applications/mobilenet/)
- [GlobalAveragePooling2D Documentation](https://keras.io/api/layers/pooling_layers/global_average_pooling2d/)
- [Dense Layer Documentation](https://keras.io/api/layers/core_layers/dense/)

onelinerhub: [How can I use the Python Keras Applications library to build a neural network?](https://onelinerhub.com/python-keras/how-can-i-use-the-python-keras-applications-library-to-build-a-neural-network)