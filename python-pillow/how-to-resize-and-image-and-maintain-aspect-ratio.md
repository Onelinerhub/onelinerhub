# How to resize and image and maintain aspect ratio

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
width = 100
height = width * im.size[1]/im.size[0]
im = im.resize((width, height))

im.show()
```


group: resize

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
width = 100
height = width * im.size[1]/im.size[0]
im = im.resize((width, height))

im.show()
```

