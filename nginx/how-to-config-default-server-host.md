# How to config default server host

```nginx
server {
  listen 80 default_server;
  # ...
}
```

- `server {` - virtual server configuration block
- `listen 80` - listen to 80 port (standard HTTP protocol)
- `default_server` - will make sure this config is used for all requests that doesn't match any configured hosts


