# How to center align text horizontally

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
W,H = im.size
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 100)

text = "I am hero"
_, _, w, h = dr.textbbox((0, 0), text, font=ft)
dr.text(((W-w)/2, 50), text, font=ft, fill=(200, 200, 0))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `ImageDraw.Draw` - create drawing object
- `ImageFont.truetype` - create font object, with font and size we're going to use for text
- `I am hero` - text to print
- `.textbbox(` - get size of a given text that will be drawn using given font
- `.text(` - draws text with given params
- `(W-w)/2` - calculate left position so that the text will be in the center of an image
- `.show()` - displays resulting image

group: text-align

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
W,H = im.size
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 100)

text = "I am hero"
_, _, w, h = dr.textbbox((0, 0), text, font=ft)
dr.text(((W-w)/2, 50), text, font=ft, fill=(200, 200, 0))

im.show()
```

