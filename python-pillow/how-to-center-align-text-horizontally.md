# How to center align text horizontally

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('/var/www/examples/heroine.png')
dr = ImageDraw.Draw(im)
ft = ImageFont.truetype('/var/www/examples/roboto.ttf', 160)
dr.text((50, 50), "I am hero", font=ft, fill=(200, 200, 0))

im.show()
```


group: text-align


