# How can I use GPU support with Python TensorFlow?
// plain

Using GPU support with Python TensorFlow requires a few steps:

1. Install the GPU version of TensorFlow: `pip install tensorflow-gpu`
2. Configure your system for GPU support:
   - Install the appropriate NVIDIA CUDA and cuDNN libraries for your system
   - Set the environment variables `CUDA_HOME` and `CUDA_VISIBLE_DEVICES`
3. Check if your system is using the GPU:
   ```python
   from tensorflow.python.client import device_lib
   print(device_lib.list_local_devices())
   ```
   Output:
   ```
   [name: "/device:CPU:0"
   device_type: "CPU"
   memory_limit: 268435456
   locality {
   }
   incarnation: 15431938337512452352, name: "/device:GPU:0"
   device_type: "GPU"
   memory_limit: 4930941747
   locality {
   bus_id: 1
   links {
   }
   }
   incarnation: 12773568187716142553
   physical_device_desc: "device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1"]
   ```
4. Use the GPU for training:
   ```python
   with tf.device('/device:GPU:0'):
       # Your code here
   ```

## Helpful links
- [TensorFlow GPU Support](https://www.tensorflow.org/install/gpu)
- [Configuring a GPU-enabled System](https://www.tensorflow.org/install/gpu#configuring_a_gpu_enabled_system)

onelinerhub: [How can I use GPU support with Python TensorFlow?](https://onelinerhub.com/python-tensorflow/how-can-i-use-gpu-support-with-python-tensorflow)