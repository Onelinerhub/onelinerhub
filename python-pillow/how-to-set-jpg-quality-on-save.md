# How to set JPG quality on save

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im.save('out.jpg', quality=95)
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.save(` - saves image under given path (format is automatically picked based on file extension)
- `quality` - sets JPG quality value
- `95` - quality value to use (where `100` is the best quality while lower values = worse quality)

group: compress


