# How to rotate image

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = im.rotate(90)

im.show()
```



