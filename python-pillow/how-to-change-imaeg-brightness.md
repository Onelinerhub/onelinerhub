# How to change imaeg brightness

```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = ImageEnhance.Brightness(im).enhace(1.5)

im.show()
```


## Example: 
```python
from PIL import Image, ImageEnhance

im = Image.open('/var/www/examples/heroine.png')
im = ImageEnhance.Brightness(im).enhace(1.5)

im.show()
```

