# How to center align text horizontally

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


group: text-align

## Example: 
```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
W,H = im.shape
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 160)

text = "I am hero"
_, _, w, h = dr.textbbox((0, 0), text, font=ft)
dr.text(((W-w)/2, (H-h)/2), text, font=ft, fill=(200, 200, 0))

im.show()
```

