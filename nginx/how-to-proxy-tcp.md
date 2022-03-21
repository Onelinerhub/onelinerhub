# How to proxy TCP

```nginx
stream {
  server {
    listen 1234;
    proxy_pass 1.2.3.4:4321;
  }
}
```

- `stream {` - stream block allows proxying `TCP` and `UDP` traffic (should be placed on the same level as `http` block)
- `server {` - virtual server configuration block
- `listen 1234` - listen to TCP traffic on localhost `1234` port
- `proxy_pass` - pass TCP traffic to the specified server
- `1.2.3.4:4321` - server host/port to proxy TCP traffic to

group: proxy


