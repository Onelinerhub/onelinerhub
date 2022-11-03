# How to add watermark to image

### To add watermark, we first make it transparent with `putalpha()` and then merge our initial image with it:

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im_merge = Image.open('/var/www/examples/watermark.png')
im_merge.putalpha(100)

im.paste(im_merge, (0, 0), im_merge)

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.putalpha(` - change transparency of an image
- `.paste(` - paste given image to the current image
- `(0, 0)` - coordinates to place watermark at
- `.show()` - displays resulting image

group: merge

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im_merge = Image.open('/var/www/examples/watermark.png')
im_merge.putalpha(100)

im.paste(im_merge, (0, 0), im_merge)

im.show()
```

