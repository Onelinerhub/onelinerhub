# Using proxy_pass

```nginx
server {
  location /api/ {
    proxy_pass http://1.2.3.4:8888;
  }
}
```

- `server {` - virtual server configuration block
- `location /api/ {` - location block will be triggered when `/api/...` request is made
- `proxy_pass` - send this request to the following upstream (other server)
- `http://1.2.3.4:8888` - server host and port to send request to

group: proxy


