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



