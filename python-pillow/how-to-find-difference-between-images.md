# How to find difference between images

```python
from PIL import Image, ImageChops

im1 = Image.open('/var/www/examples/heroine.png').convert('RGBA')
im2 = Image.open('/var/www/examples/hero.png').convert('RGBA')
diff = ImageChops.difference(im1, im2)

if len(diff.getdata()) > 0:
  print('Images are different, yes')
```


## Example: 
```python
from PIL import Image, ImageChops

im1 = Image.open('/var/www/examples/heroine.png').convert('RGBA')
im2 = Image.open('/var/www/examples/hero.png').convert('RGBA')
diff = ImageChops.difference(im1, im2)

print(len(diff.getdata()))
```
```
806300

```

