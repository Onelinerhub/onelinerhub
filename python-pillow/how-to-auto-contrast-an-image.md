# How to auto contrast an image

```python
from PIL import Image, ImageOps

im = Image.open('/var/www/examples/heroine.png')
im = ImageOps.autocontrast(im, cutoff = 2, ignore = 2)
im.show()
```


group: contrast


