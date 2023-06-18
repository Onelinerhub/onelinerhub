# How do I access the applications attribute in the tensorflow.python.keras module?
// plain

To access the applications attribute in the tensorflow.python.keras module, you must first import the module. This can be done with the following code:

```
import tensorflow.python.keras as keras
```

The applications attribute is a submodule of the keras module. You can access this attribute with the following code:

```
applications = keras.applications
```

The applications submodule contains several pre-trained models for deep learning, such as VGG16, ResNet50, and MobileNetV2. These models can be used for image classification, object detection, and more. To use one of these models, you can call the model function with the desired model name as an argument:

```
model = applications.VGG16()
```

The model function returns a Keras Model object, which can be used to perform inference on data.

## Code explanation


1. `import tensorflow.python.keras as keras`: imports the tensorflow.python.keras module as the object `keras`.
2. `applications = keras.applications`: accesses the applications attribute of the keras module, storing it in the variable `applications`.
3. `model = applications.VGG16()`: calls the model function of the applications module, passing the string `VGG16` as an argument. This returns a Keras Model object and stores it in the variable `model`.

## Helpful links

- [Keras Applications](https://keras.io/applications/)
- [TensorFlow Keras API](https://www.tensorflow.org/api_docs/python/tf/keras)

onelinerhub: [How do I access the applications attribute in the tensorflow.python.keras module?](https://onelinerhub.com/python-tensorflow/how-do-i-access-the-applications-attribute-in-the-tensorflow-python-keras-module)