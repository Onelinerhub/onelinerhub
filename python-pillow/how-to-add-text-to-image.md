# How to add text to image

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
W,H = im.shape
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 160)

text = "I am hero"
_, _, w, h = draw.textbbox((0, 0), text, font=ft)
dr.text(((W-w)/2, (H-h)/2), text, font=ft, fill=(200, 200, 0))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `ImageDraw.Draw` - create drawing object
- `ImageFont.truetype` - create font object, with font and size we're going to use for text
- `160` - font size to use for our text
- `.text(` - draws text with given params
- `(50, 50)` - text top left corner coordinates
- `I am hero` - text to print
- `font=ft` - we use font that we've declared earlier
- `(200, 200, 0)` - RGB representation of a color to use for text
- `.show()` - displays resulting image

group: text

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 160)
dr.text((50, 50), "I am hero", font=ft, fill=(200, 200, 0))

im.show()
```

