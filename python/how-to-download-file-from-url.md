# How to download file from url

```python
import requests

r = requests.get('https://www.wikipedia.org/', allow_redirects=True)

with open('/tmp/index.html', 'wb') as f:
  f.write(r.content)
```

- `requests` - module to work with HTTP requests
- `requests.get` - will get content from specified URL
- `https://www.wikipedia.org/` - URL to get content from
- `allow_redirects` - enables (or disables) following redirects
- `/tmp/index.html` - resulting file that will contain downloaded content
- `f.write` - write content to the file
- `r.content` - downloaded content


## Additional keywords
- web
- www
- online
