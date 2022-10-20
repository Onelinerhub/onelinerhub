# Pillow usage example

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = im.resize((100, 100))
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `.resize(` - resizes given image to the specified size
- `.show()` - displays resulting image

group: install

## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = im.resize((100, 100))
im.show()
```

