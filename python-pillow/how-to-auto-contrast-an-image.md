# How to auto contrast an image

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')

im = ImageOps.autocontrast(im, cutoff = 5)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `ImageOps.autocontrast` - set contrast automatically based on given cutoff
- `cutoff = 5` - defines part of histogram (in percents) that should be removed
- `.show()` - displays resulting image

group: contrast

## Example: 
```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.autocontrast(im, cutoff = 5)
im.show()
```

