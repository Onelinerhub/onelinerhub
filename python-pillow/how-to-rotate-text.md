# How to rotate text

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
text = "I am hero"

tim = Image.new('L', (800,400))
dr = ImageDraw.Draw(tim)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 100)
dr.text(((W-w)/2, 50), text, font=ft, fill=(200, 200, 0))

tim = txt.rotate(45,  expand=1)

im.paste(tim, (0,0))
im.show()
```


group: text

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
text = "I am hero"

tim = Image.new('L', (800,400))
dr = ImageDraw.Draw(tim)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 100)
dr.text(((W-w)/2, 50), text, font=ft, fill=(200, 200, 0))

tim = txt.rotate(45,  expand=1)

im.paste(tim, (0,0))
im.show()
```

