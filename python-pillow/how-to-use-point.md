# How to map image using point() method

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = im.point(lambda p: p > 100 and 255)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.point(` - maps an image with a given callback
- `p > 100 and 255` - trims colors beyond value of 100 and returns 255
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = im.point(lambda p: p > 100 and 255)
im.show()
```

