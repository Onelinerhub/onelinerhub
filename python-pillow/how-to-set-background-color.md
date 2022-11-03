# How to set background color

### Background is set as a `color` argument of `Image.new` method:

```python
from PIL import Image, ImageFilter

im = Image.new(mode='RGB', size=(300,300), color=(150,200,50))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `mode='RGB'` - create new image in `RGB` color mode
- `(300,300)` - new image width and height
- `(150,200,50)` - background color in `RGB` tuple
- `.show()` - displays resulting image

group: create

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.new(mode='RGB', size=(300,300), color=(150,200,50))

im.show()
```

