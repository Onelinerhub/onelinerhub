# How do I use TensorFlow with Python 3.11?
// plain

Using TensorFlow with Python 3.11 is easy and straightforward. The following example code block will help you get started:

```
#import tensorflow
import tensorflow as tf

#create a constant
constant = tf.constant(2.0, dtype=tf.float32)

#create a variable
variable = tf.Variable([3.0], dtype=tf.float32)

#add the two
sum = tf.add(constant, variable)

#print the result
print(sum)
```
The output of this code block will be:
```
tf.Tensor([5.], shape=(1,), dtype=float32)
```

The code consists of the following parts:

1. **Import TensorFlow**: The first line imports TensorFlow as tf.
2. **Create a constant**: The second line creates a constant with a value of 2.0 and a data type of tf.float32.
3. **Create a variable**: The third line creates a variable with a value of 3.0 and a data type of tf.float32.
4. **Add the two**: The fourth line adds the constant and the variable together.
5. **Print the result**: The fifth line prints the result of the addition.

For more information on using TensorFlow with Python 3.11, please refer to the [TensorFlow documentation](https://www.tensorflow.org/tutorials/).

onelinerhub: [How do I use TensorFlow with Python 3.11?](https://onelinerhub.com/python-tensorflow/how-do-i-use-tensorflow-with-python-----)