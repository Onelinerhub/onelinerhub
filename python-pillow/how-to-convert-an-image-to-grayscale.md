# How to convert an image to grayscale

```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert('L')

im.show()
```


group: black_white

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.open('/var/www/examples/heroine.png')
im = im.convert('L')

im.show()
```

