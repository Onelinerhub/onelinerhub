# How can I enable GPU support for TensorFlow in Python?
// plain

To enable GPU support for TensorFlow in Python, you'll need to have an NVIDIA GPU with a compute capability of at least 3.5. You'll also need to install the NVIDIA CUDA Toolkit and cuDNN library.

Once you have the necessary software installed, you can enable GPU support in TensorFlow by setting the GPU option in the `tf.compat.v1.ConfigProto` configuration object:

```
import tensorflow as tf

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)
```

The code above will allow TensorFlow to dynamically allocate memory to the GPU as needed.

You can also specify a fraction of the total memory to be allocated to the GPU by setting the `per_process_gpu_memory_fraction` option:

```
import tensorflow as tf

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
sess = tf.compat.v1.Session(config=config)
```

This will allocate 50% of the total GPU memory to TensorFlow.

To check if GPU support is enabled, you can run the following code:

```
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())
```

The output should show the available GPUs:

```
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 9096227255976374448, name: "/device:XLA_GPU:0"
device_type: "XLA_GPU"
memory_limit: 17179869184
locality {
}
incarnation: 7333547481407717232
physical_device_desc: "device: XLA_GPU device", name: "/device:GPU:0"
device_type: "GPU"
memory_limit: 15956161332
locality {
  bus_id: 1
  links {
  }
}
incarnation: 17361726204518689034
physical_device_desc: "device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1"]
```

For more information, please refer to the [TensorFlow documentation](https://www.tensorflow.org/guide/gpu).

onelinerhub: [How can I enable GPU support for TensorFlow in Python?](https://onelinerhub.com/python-tensorflow/how-can-i-enable-gpu-support-for-tensorflow-in-python)