# How to add noise

```python
from PIL import Image, ImageFilter, random

im = Image.open('/var/www/examples/heroine.png')
im[0][0]=255

im.show()
```


group: noise


