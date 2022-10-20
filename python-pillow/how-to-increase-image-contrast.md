# How to increase image contrast

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')

im = ImageEnhance.Contrast(im).enhance(1.5)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `/var/www/examples/heroine.png` - path to sample image to open
- `ImageEnhance.Contrast` - object to manipulate image contrast
- `.enhance(` - increases contrast to a given value
- `1.5` - we'll increase contrast by `50%`
- `.show()` - displays resulting image

group: contrast


