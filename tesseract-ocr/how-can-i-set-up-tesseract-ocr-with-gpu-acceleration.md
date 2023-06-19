# How can I set up tesseract OCR with GPU acceleration?
// plain

1. Install [CUDA](https://developer.nvidia.com/cuda-downloads) and [cuDNN](https://developer.nvidia.com/cudnn) according to your GPU type.

2. Install [tesseract-ocr](https://github.com/tesseract-ocr/tesseract) with GPU acceleration enabled:
```
$ git clone https://github.com/tesseract-ocr/tesseract
$ cd tesseract
$ ./autogen.sh
$ ./configure --enable-gpu --with-cuda-dir=/usr/local/cuda --with-cudnn-dir=/usr/local/cudnn
$ make
$ sudo make install
```

3. Test GPU acceleration:
```
$ tesseract --list-langs
```
## Output example

```
List of available languages (4):
eng
osd
```

4. Set environment variables:
```
$ export TESSERACT_ENABLE_GPU=1
$ export TESSERACT_GPU_EXECUTABLE=/usr/local/cuda/bin/nvcc
```

5. Run tesseract with GPU acceleration:
```
$ tesseract --oem 1 --psm 3 --tessdata-dir /usr/local/share/tessdata <image> <output>
```

6. Check the GPU usage with `nvidia-smi` command.

7. For more information, see the [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki/GPU-Acceleration).

onelinerhub: [How can I set up tesseract OCR with GPU acceleration?](https://onelinerhub.com/tesseract-ocr/how-can-i-set-up-tesseract-ocr-with-gpu-acceleration)