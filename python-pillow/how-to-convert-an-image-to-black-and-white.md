# How to convert an image to black and white

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert('1')

im.show()
```


group: black_white

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert('1')

im.show()
```

