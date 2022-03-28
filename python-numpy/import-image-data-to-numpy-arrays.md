# Import image data to Numpy array

```python
import numpy as np
from PIL import Image

image = Image.open('/var/www/examples/heroine.png')
data = np.asarray(image)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `from PIL import Image` - load [lib: Pillow module](/python-pillow/how-to-install-python-pillow-module) to work with images
- `Image.open` - loads given image into `image` array
- `/var/www/examples/heroine.png` - path to image to load
- `np.asarray` - load Numpy array data from given data treated as array
- `data` - will contain data loaded from image

group: image

## Example: 
```python
import numpy as np
from PIL import Image

image = Image.open('/var/www/examples/heroine.png')
data = np.asarray(image)

print(data.shape)
print(data[1][3][154])
```
```
(1100, 733, 3)

```

