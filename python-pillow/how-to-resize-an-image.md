# How to resize an image

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.resize((100, 200))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.resize(` - resizes given image to the specified size
- `100` - resized image width
- `200` - resized image height
- `.show()` - displays resulting image

group: resize

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.resize((100, 150))

im.show()
```

