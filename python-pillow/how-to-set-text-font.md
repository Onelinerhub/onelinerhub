# How to set text font

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 160)
dr.text((50, 50), "I am hero", font=ft, fill=(200, 200, 0))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `ImageFont.truetype` - create font object, with font and size we're going to use for text
- `/var/www/examples/roboto.ttf` - path to font to use
- `160` - font size to use
- `.text(` - draws text with given params

group: text


