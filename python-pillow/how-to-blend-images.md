# How to blend images

```python
from PIL import Image

im1 = Image.open('/var/www/examples/heroine.png')
im2 = Image.open('/var/www/examples/hero.png')

im = Image.blend(im1, im2, 0.5)
im.show()
```


group: merge


