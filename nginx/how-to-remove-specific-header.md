# How to remove specific header

```nginx
server {
  location / {
    proxy_pass http://backend;
    proxy_hide_header X-My-Header;
  }
}
```

- `server {` - virtual server configuration block
- `location / {` - default location block that will be triggered on all requests
- `http://backend` - sample backend to proxy to
- `proxy_hide_header` - will remove specified headers from proxy response
- `X-My-Header` - sample header to remove from response


