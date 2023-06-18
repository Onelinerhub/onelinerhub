# How can I use Python and SciPy to run computations on a GPU?
// plain

Using Python and SciPy to run computations on a GPU requires the installation of a few packages. Specifically, you will need to install [PyCUDA](https://mathema.tician.de/software/pycuda/), [SciPy-CUDA](https://github.com/lebedov/scipy-cuda) and [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

Once these packages are installed, you can start running computations on the GPU. For example, to calculate the sum of two matrices, you can use the following code:

```
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import numpy

# Initialize the CUDA device
cuda.init()

# Create two random matrices
a = numpy.random.randn(4,4).astype(numpy.float32)
b = numpy.random.randn(4,4).astype(numpy.float32)

# Transfer host (CPU) memory to device (GPU) memory
a_gpu = gpuarray.to_gpu(a)
b_gpu = gpuarray.to_gpu(b)

# Perform the calculation on the GPU
c_gpu = a_gpu + b_gpu

# Transfer result back to host (CPU)
c_cpu = c_gpu.get()

# Print the results
print(c_cpu)
```

## Output example

```
[[-1.38693988 -0.63866985 -0.63716674 -1.45010793]
 [-0.48002441  0.71717268  0.7676481  -0.45486873]
 [ 0.73513508 -1.93739796  0.20775067 -0.84748602]
 [ 0.43687046  0.08488413 -1.078195   -1.61167681]]
```

Here is a breakdown of the code:

1. `import pycuda.gpuarray as gpuarray`: imports the `gpuarray` module which allows us to transfer data between the CPU and GPU.
2. `import pycuda.driver as cuda`: imports the `cuda` module which allows us to initialize the CUDA device.
3. `import numpy`: imports the `numpy` module which allows us to generate random matrices.
4. `cuda.init()`: initializes the CUDA device.
5. `a = numpy.random.randn(4,4).astype(numpy.float32)`: creates a random 4x4 matrix of type `float32`.
6. `b = numpy.random.randn(4,4).astype(numpy.float32)`: creates a second random 4x4 matrix of type `float32`.
7. `a_gpu = gpuarray.to_gpu(a)`: transfers the matrix `a` from the CPU to the GPU.
8. `b_gpu = gpuarray.to_gpu(b)`: transfers the matrix `b` from the CPU to the GPU.
9. `c_gpu = a_gpu + b_gpu`: performs the calculation of the sum of `a` and `b` on the GPU.
10. `c_cpu = c_gpu.get()`: transfers the result of the calculation back to the CPU.
11. `print(c_cpu)`: prints the result of the calculation.

For more information, please refer to the [PyCUDA documentation](https://mathema.tician.de/software/pycuda/), the [SciPy-CUDA documentation](https://github.com/lebedov/scipy-cuda) and the [CUDA Toolkit documentation](https://developer.nvidia.com/cuda-toolkit).

onelinerhub: [How can I use Python and SciPy to run computations on a GPU?](https://onelinerhub.com/python-scipy/how-can-i-use-python-and-scipy-to-run-computations-on-a-gpu)