# Using mask to merge two images

```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im_merge = Image.open('/var/www/examples/hammer.png')

im.paste(im_merge, (0, 0))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.open` - open given image with Pillow
- `.paste(` - paste given image to the current image
- `im_merge` - image to paste to `im`
- `(0, 0)` - `x` and `y` coordinates to paste image to
- `.show()` - displays resulting image

group: merge

## Example: 
```python
from PIL import Image

im = Image.open('/var/www/examples/heroine.png')
im_merge = Image.open('/var/www/examples/hammer.png')

im.paste(im_merge, (0, 0))

im.show()
```

