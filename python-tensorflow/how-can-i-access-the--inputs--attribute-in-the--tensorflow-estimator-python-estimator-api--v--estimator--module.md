# How can I access the 'inputs' attribute in the 'tensorflow_estimator.python.estimator.api._v2.estimator' module?
// plain

The `inputs` attribute in the `tensorflow_estimator.python.estimator.api._v2.estimator` module can be accessed by creating an instance of the `tf.estimator.Estimator` class. This class takes in a model function that defines the model's architecture, as well as a set of `tf.estimator.RunConfig` objects that define the runtime environment for the estimator. The `inputs` attribute can then be accessed by calling the `inputs` method on the `tf.estimator.Estimator` instance.

## Example code


```
import tensorflow as tf

def my_model_fn(features, labels, mode):
    # define model architecture
    pass

run_config = tf.estimator.RunConfig(model_dir='/tmp/model_dir')
estimator = tf.estimator.Estimator(model_fn=my_model_fn, config=run_config)
inputs = estimator.inputs
```

## Code explanation


- `import tensorflow as tf`: imports the TensorFlow library into the current Python environment.
- `def my_model_fn(features, labels, mode):`: defines a model function that takes in feature data, label data, and a mode (train, evaluate, or predict) as input arguments.
- `run_config = tf.estimator.RunConfig(model_dir='/tmp/model_dir')`: creates a `tf.estimator.RunConfig` object that defines the runtime environment for the estimator.
- `estimator = tf.estimator.Estimator(model_fn=my_model_fn, config=run_config)`: creates an instance of the `tf.estimator.Estimator` class using the model function and runtime environment defined above.
- `inputs = estimator.inputs`: accesses the `inputs` attribute of the `tf.estimator.Estimator` instance.

## Helpful links

- [TensorFlow Estimators](https://www.tensorflow.org/guide/estimators)
- [tf.estimator.Estimator](https://www.tensorflow.org/api_docs/python/tf/estimator/Estimator)

onelinerhub: [How can I access the 'inputs' attribute in the 'tensorflow_estimator.python.estimator.api._v2.estimator' module?](https://onelinerhub.com/python-tensorflow/how-can-i-access-the--inputs--attribute-in-the--tensorflow-estimator-python-estimator-api--v--estimator--module)