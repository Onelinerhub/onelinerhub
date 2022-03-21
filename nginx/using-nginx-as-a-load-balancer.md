# Using Nginx as a load balancer

```nginx
upstream backend {
  least_conn;
  server 1.2.3.4 weight=3;
  server 2.3.4.5 weight=1;
  server 4.3.2.1 backup;
}
server {
  location / {
    proxy_pass http://backend;
  }
}
```

- `upstream backend {` - specify list of server to balance requests to
- `weight=3` - use this server 3 times more frequent as the following one (the one with `weight=1`)
- `backup` - this server will be only used when previous 2 servers are offline
- `server {` - virtual server configuration block
- `location / {` - default location block
- `proxy_pass http://backend;` - process request using load balancing
- `least_conn` - will pick server from the list with least active connections

group: balancing


