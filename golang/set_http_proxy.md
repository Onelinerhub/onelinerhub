# Use proxy in net/http or any other Go HTTP package

```Go
import os

os.Setenv("HTTP_PROXY", "http://proxy_username:proxy_password@example_proxy.io:port")
```

- username and password can be omitted if the proxy doesn't require authentication
- you can use `os.Unsetenv("HTTP_PROXY")` to unset proxy for some scopes
