# How to use proxy

```python
import requests
r = requests.get('https://google.com', proxies={"http":"http://host:port"})
html = r.content
```

- `import requests` - library to work with http requests
- `requests.get` - get content by specified URL
- `proxies=` - use specified proxy
- `host:port` - host/port of the proxy to use
- `r.content` - returns html of finished request

