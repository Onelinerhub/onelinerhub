# Import image data to Numpy arrays

```python
import numpy as np
from PIL import Image

image = Image.open('/var/www/examples/heroine.png')
print(image.format)
print(image.size)
print(image.mode)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `from PIL import Image` - load [lib: Pillow module](/python-pillow/how-to-install-python-pillow-module) to work with images

group: image

## Example: 
```python
import numpy as np
from PIL import Image

image = Image.open('/var/www/examples/heroine.png')
print(image.format)
print(image.size)
print(image.mode)
```

