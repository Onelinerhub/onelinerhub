# How to blend images

```python
from PIL import Image

im1 = Image.open('/var/www/examples/heroine.png').convert('RGBA')
im2 = Image.open('/var/www/examples/hero.png').convert('RGBA')

im = Image.blend(im1, im2, 0.5)
im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.convert('RGBA')` - we need to use alpha channel (opacity) to blend images, so this needs to be done
- `Image.blend(` - blends 2 images with a given level of transparency
- `im1, im2` - images to blend
- `0.5` - transparency level (`50%` in our case)
- `.show()` - displays resulting image

group: merge

## Example: 
```python
from PIL import Image

im1 = Image.open('/var/www/examples/heroine.png').convert('RGBA')
im2 = Image.open('/var/www/examples/hero.png').convert('RGBA')

im = Image.blend(im1, im2, 0.5)
im.show()
```

