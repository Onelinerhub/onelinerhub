# How to create an image

```python
from PIL import Image, ImageFilter

im = Image.new(mode='RGB', size=(100,100), color=(100,50,150))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `Image.new` - create new `PIL` image object
- `mode='RGB'` - create new image in `RGB` color mode
- `(100,100)` - new image will be `100x100`
- `(100,50,150)` - color to use for background in `RGB` tuple form
- `.show()` - displays resulting image

group: create

## Example: 
```python
from PIL import Image, ImageFilter

im = Image.new(mode='RGB', size=(100,100), color=(100,50,150))

im.show()
```

