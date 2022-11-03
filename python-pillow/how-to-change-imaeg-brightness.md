# How to change image brightness

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = ImageEnhance.Brightness(im).enhance(2)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `ImageEnhance.Brightness` - brightness management utility
- `enhance` - changes respective enhance option (brightness in our case)
- `2` - increases brightness by 2 times
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = ImageEnhance.Brightness(im).enhance(2)

im.show()
```

