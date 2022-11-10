# How to get array from image

```python
from PIL import Image
import numpy as np

im = Image.open('/var/www/examples/heroine.png')
data = np.asarray(im)
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `np.asarray` - converts given `im` image to array

group: array

## Example: 
```python
from PIL import Image
import numpy as np

im = Image.open('/var/www/examples/heroine.png')
data = np.asarray(im)

print(data[1][2])
```
```
[154 168 153]

```

