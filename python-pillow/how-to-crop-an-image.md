# How to crop an image

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.crop((100, 100, 400, 800))

im.show()
```


group: crop

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.crop((100, 100, 400, 800))

im.show()
```

