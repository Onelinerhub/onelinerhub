# Use proxy in net/http or any other Go HTTP package

```Go
import os
os.Setenv("HTTP_PROXY", "http://proxy_username:proxy_password@example_proxy.io:port")
```

- import os - include operating-system level library
- os.Setenv - sets environment variable to enable proxying (use ```os.Unsetenv("HTTP_PROXY")``` to unset proxy for some scopes)
- proxy_username - proxy auth user (can be omitted if the proxy doesn't require authentication)
- proxy_password - proxy auth pwd (can be omitted if the proxy doesn't require authentication)
- example_proxy.io:port - proxy host and port
