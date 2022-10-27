# How to create thumbnail

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im.thumbnail((100, 100))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.thumbnail(` - creates image thumbnail that fits into given width/height
- `100, 100` - thumbnail width and height
- `.show()` - displays resulting image

group: resize

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im.thumbnail((100, 100))

im.show()
```

