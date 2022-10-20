# How to add text to image

```python
from PIL import Image, ImageDraw

im = Image.open('/var/www/examples/heroine.png')
dr = ImageDraw.Draw(im)
dr.text((100, 100), "I am hero", fill=(200, 100, 0))

im.show()
```


group: text


