# How can I use a GPU with Python TensorFlow?
// plain

Using a GPU with Python TensorFlow is relatively straightforward and can provide a significant speedup over using a CPU. To use a GPU with TensorFlow, you must have a supported GPU with a compatible driver installed.

Example code to check if the GPU is available and visible to TensorFlow:

```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

## Output example

```
[name: "/device:CPU:0"
 device_type: "CPU"
 memory_limit: 268435456
 locality {
 }
 incarnation: 12097170122906550962, name: "/device:GPU:0"
 device_type: "GPU"
 memory_limit: 4930941747
 locality {
   bus_id: 1
   links {
   }
 }
 incarnation: 14582080206794650090
 physical_device_desc: "device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1"]
```

The code above prints a list of local devices, including the CPU and any GPUs available.

To use a GPU with TensorFlow, you must specify which GPU to use when creating a session. Example code to create a session on GPU 0:

```
import tensorflow as tf

with tf.Session() as sess:
  with tf.device("/GPU:0"):
    # Create model
    ...
    # Run model
    ...
```

The code above creates a session on GPU 0, and any operations created within that session will be placed on GPU 0.

## Helpful links
- [TensorFlow GPU Support](https://www.tensorflow.org/install/gpu)
- [Using GPUs](https://www.tensorflow.org/guide/using_gpu)

onelinerhub: [How can I use a GPU with Python TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-use-a-gpu-with-python-tensorflow-1687086298)