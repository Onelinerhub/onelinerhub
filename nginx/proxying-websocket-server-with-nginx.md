# Proxying websocket server with Nginx

```nginx
map $http_upgrade $connection_upgrade {
  default Upgrade;
  '' close;
}

server {
  location /ws/ {
    proxy_pass http://1.2.3.4:8010;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header Host $host;
  }
}
```

- `server {` - virtual server configuration block
- `location /ws/ {` - this location block will be triggered for all `/ws/...` requests
- `1.2.3.4:8010` - server and port for our websocket server to proxy to
- `Upgrade $http_upgrade` - add `Upgrade` header to send to websocket server
- `Connection $connection_upgrade` - add `Connection` header to send to websocket server
- `Host $host` - use the same `Host` header for websocket

group: proxy


