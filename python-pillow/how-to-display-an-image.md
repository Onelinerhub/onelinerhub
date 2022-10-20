# How to display an image

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')

im.show()
```

- `Image.open` - open given image with Pillow
- `.show()` - displays resulting image


