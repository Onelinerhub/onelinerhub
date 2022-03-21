# Configure load balancing health checks

```nginx
upstream backend {
  server 1.2.3.4;
  server 2.3.4.5;
}
server {
  location / {
    proxy_pass http://backend;
    health_check interval=2 fails=2 passes=2;
  }
}
```

- `upstream backend {` - specify list of server to balance requests to
- `server {` - virtual server configuration block
- `location / {` - default location block
- `proxy_pass http://backend;` - process request using load balancing
- `health_check` - specify health check rules
- `interval=2` - run health check every `2` seconds
- `fails=2` - mark server as unhealthy if `2` consecutive check fail
- `passes=2` - server will be marked as healthy again if `2` consecutive checks succeed

group: balancing


