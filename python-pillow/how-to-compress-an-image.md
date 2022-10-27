# How to compress an image

### Compression level can be increased by lowering `quality` value:

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im.save('out.jpg', quality=75)
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.save(` - saves image under given path (format is automatically picked based on file extension)
- `quality` - sets JPG quality value (lower quality values reduce file size)
- `75` - out of `100`, use lower values to reduce file size even more

group: compress


