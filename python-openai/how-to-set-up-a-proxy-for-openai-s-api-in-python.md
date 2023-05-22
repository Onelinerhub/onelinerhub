# How to set up a proxy for OpenAI's API in Python?
// plain

Setting up a proxy for OpenAI's API in Python is easy.

```
import os
os.environ['http_proxy'] = 'http://username:password@proxy.example.com:8080'
os.environ['https_proxy'] = 'https://username:password@proxy.example.com:8080'
```

This code sets up the environment variables `http_proxy` and `https_proxy` with the proxy server address and credentials.

## Code explanation


- `import os`: imports the `os` module which provides functions for interacting with the operating system.
- `os.environ['http_proxy']`: sets the environment variable `http_proxy` with the proxy server address and credentials.
- `os.environ['https_proxy']`: sets the environment variable `https_proxy` with the proxy server address and credentials.

## Helpful links

- [Python os Module](https://docs.python.org/3/library/os.html)

onelinerhub: [How to set up a proxy for OpenAI's API in Python?](https://onelinerhub.com/python-openai/how-to-set-up-a-proxy-for-openai-s-api-in-python)