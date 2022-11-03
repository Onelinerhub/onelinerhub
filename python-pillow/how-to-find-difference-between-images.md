# How to find difference between images

```python
from PIL import Image, ImageChops

im1 = Image.open('/var/www/examples/heroine.png')
im2 = Image.open('/var/www/examples/hero.png')
diff = ImageChops.difference(im1, im2)

print(diff.getbox())
```


## Example: 
```python
from PIL import Image, ImageChops

im1 = Image.open('/var/www/examples/heroine.png')
im2 = Image.open('/var/www/examples/hero.png')
diff = ImageChops.difference(im1, im2)

print(diff.getbox())
```

