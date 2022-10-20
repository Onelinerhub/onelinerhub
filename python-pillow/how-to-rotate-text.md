# How to rotate text

### We can't draw rotated text, but we can create separate image and draw text there. Then rotate that separate image and merge it with our original image:

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
text = "I am hero"

tim = Image.new('RGBA', (500,200), (0,0,0,0))
dr = ImageDraw.Draw(tim)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 100)
dr.text((0, 0), text, font=ft, fill=(200, 200, 0))

tim = tim.rotate(30,  expand=1)

im.paste(tim, (0,0), tim)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `I am hero` - text to print
- `Image.new` - create new `PIL` image object
- `(0,0,0,0)` - we create an image with transparent background
- `ImageDraw.Draw` - create drawing object
- `ImageFont.truetype` - create font object, with font and size we're going to use for text
- `.text(` - draws text with given params
- `.rotate(` - rotate given image
- `30` - rotate by 30 degrees
- `expand=1` - expand image if rotated image can't fit into initial size
- `.paste(` - paste image with text on top of loaded image
- `.show()` - displays resulting image

group: text

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
text = "I am hero"

tim = Image.new('RGBA', (500,200), (0,0,0,0))
dr = ImageDraw.Draw(tim)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 100)
dr.text((0, 0), text, font=ft, fill=(200, 200, 0))

tim = tim.rotate(30,  expand=1)

im.paste(tim, (0,0), tim)
im.show()
```

