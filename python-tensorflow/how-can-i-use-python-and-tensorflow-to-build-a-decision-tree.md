# How can I use Python and TensorFlow to build a decision tree?
// plain

In order to use Python and TensorFlow to build a decision tree, you need to first install TensorFlow on your machine. After that, you can use the [`tf.contrib.learn.DNNClassifier`](https://www.tensorflow.org/api_docs/python/tf/contrib/learn/DNNClassifier) class from TensorFlow to build a decision tree.

## Example code

```
# Import TensorFlow
import tensorflow as tf

# Create feature columns
feature_columns = [tf.contrib.layers.real_valued_column("x", dimension=4)]

# Create a deep neural network classifier
classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10, 20, 10],
                                            n_classes=3,
                                            model_dir="/tmp/dnn_model")

# Train the model
classifier.fit(x=X_train, y=y_train, steps=200)

# Evaluate the model
accuracy_score = classifier.evaluate(x=X_test, y=y_test)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))
```

The code above will create a deep neural network classifier with three hidden layers of 10, 20 and 10 nodes respectively. The `X_train` and `y_train` parameters will be used to train the model and the `X_test` and `y_test` parameters will be used to evaluate the model. The `accuracy_score` variable will contain the accuracy of the model.

## Helpful links
- [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf/contrib/learn/DNNClassifier)
- [Tutorial on Building Decision Trees with TensorFlow](https://www.tensorflow.org/tutorials/estimators/cnn)

onelinerhub: [How can I use Python and TensorFlow to build a decision tree?](https://onelinerhub.com/python-tensorflow/how-can-i-use-python-and-tensorflow-to-build-a-decision-tree)