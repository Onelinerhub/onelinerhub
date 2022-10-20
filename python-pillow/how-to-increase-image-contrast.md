# How to increase image contrast

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')

enh = ImageEnhance.Contrast(im)
im = enh.enhance(1.5)
im.show()
```


group: contrast


