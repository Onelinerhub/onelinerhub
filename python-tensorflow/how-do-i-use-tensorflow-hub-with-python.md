# How do I use TensorFlow Hub with Python?
// plain

TensorFlow Hub is a library for reusable machine learning modules. It enables users to reuse parts of existing TensorFlow models and to share their own creations.

Using TensorFlow Hub with Python is easy. All you need to do is install the TensorFlow Hub library and import it into your Python environment. The following code snippet shows how to do this:

```
import tensorflow_hub as hub
```

Once imported, you can use the library to access and download models from the TensorFlow Hub repository. For example, the following code snippet shows how to download a MobileNet model from TensorFlow Hub:

```
module = hub.Module("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/1")
```

You can also use the library to create your own modules. For example, the following code snippet shows how to create a module with a simple linear model:

```
module = hub.Module(function=linear_model)
```

Once you have your modules, you can use them to build TensorFlow models. For example, the following code snippet shows how to use the MobileNet model to create a TensorFlow model:

```
features = module(input_image)
logits = tf.layers.dense(features, num_classes)
```

With TensorFlow Hub, you can easily reuse existing models and create your own.

## Helpful links
- [TensorFlow Hub Documentation](https://www.tensorflow.org/hub)
- [TensorFlow Hub Tutorial](https://www.tensorflow.org/tutorials/images/hub_with_keras)

onelinerhub: [How do I use TensorFlow Hub with Python?](https://onelinerhub.com/python-tensorflow/how-do-i-use-tensorflow-hub-with-python)