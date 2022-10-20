# How to load an image from url

```python
from PIL import Image
import requests
from io import BytesIO

url = 'https://examples.onelinerhub.com/heroine.png'

response = requests.get(url)
img = Image.open(BytesIO(response.content))

im.show()
```

- `PIL` - import [lib:Pillow](https://onelinerhub.com/python-pillow/how-to-install-python-pillow-module) package modules
- `url` - url to load image from
- `requests.get` - loads data from given url
- `Image.open` - open given image with Pillow
- `BytesIO` - convert given argument to `BytesIO` object, so it can be used by `Pillow`
- `response.content` - get content previously loaded from url
- `.show()` - displays resulting image

## Example: 
```python
from PIL import Image
import requests
from io import BytesIO

url = 'https://examples.onelinerhub.com/heroine.png'

response = requests.get(url)
im = Image.open(BytesIO(response.content))

im.show()
```

