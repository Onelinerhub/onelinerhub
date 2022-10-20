# How to blur an image

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.filter(ImageFilter.BoxBlur(5))

im.show()
```


group: blur


