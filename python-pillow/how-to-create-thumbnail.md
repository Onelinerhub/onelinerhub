# How to create thumbnail

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.thumbnail((100, 100))

im.show()
```


group: resize

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
im = im.thumbnail((100, 100))

im.show()
```

