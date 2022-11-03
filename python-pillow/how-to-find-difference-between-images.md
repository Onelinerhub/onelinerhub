# How to find difference between images

```python
from PIL import Image, ImageChops

im1 = Image.open('/var/www/examples/heroine.png').convert('RGBA')
im2 = Image.open('/var/www/examples/hero.png').convert('RGBA')
diff = ImageChops.difference(im1, im2)
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `ImageChops.difference(` - calculates pixel-by-pixel difference between given images and returns it
- `diff.getdata()` - returns different

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

