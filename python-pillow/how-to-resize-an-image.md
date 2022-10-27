# How to resize an image

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.resize((100, 200))

im.show()
```


group: resize


