# How to mirror image

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.mirror(im)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `ImageOps.mirror(` - mirrors given image horizontally
- `.show()` - displays resulting image

group: flip_mirror

## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.mirror(im)

im.show()
```

