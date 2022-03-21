# Simple load balancing example

```nginx
upstream backend {
  server 1.2.3.4;
  server 2.3.4.5;
}
server {
  location / {
    proxy_pass http://backend;
  }
}
```

- `upstream backend {` - specify list of server to balance requests to
- `server {` - virtual server configuration block
- `location / {` - default location block
- `proxy_pass` - send this request to the following upstream (other server)
- `http://backend` - Nginx will automatically pick server from list of server to balance request between

group: balancing


