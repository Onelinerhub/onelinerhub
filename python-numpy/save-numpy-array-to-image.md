# Save Numpy array to image

```python
import numpy as np
from PIL import Image

image2 = Image.fromarray(data)
image2.save('/tmp/image.png')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `from PIL import Image` - load [lib: Pillow module](/python-pillow/how-to-install-python-pillow-module) to work with images
- `Image.fromarray` - load image data from given Numpy array
- `data` - Numpy array to save to image ( (e.g. [loaded from another image](/python-numpy/import-image-data-to-numpy-arrays)))
- `.save(` - save current image object into specified file

group: image

## Example: 
```python
import numpy as np
from PIL import Image

image = Image.open('/var/www/examples/heroine.png')
data = np.asarray(image)

image2 = Image.fromarray(data)
image2.save('/tmp/image.png')

print(type(image2))
```
```
<class 'PIL.Image.Image'>

```

