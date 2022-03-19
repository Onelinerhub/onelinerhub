# Setup keepalive connections

```nginx
server {
  keepalive_timeout 60s;
  keepalive_time 30m;
  keepalive_requests 1000;
  keepalive_disable msie6;
}
```

- `server {` - virtual server configuration block
- `keepalive_timeout` - sets number of seconds to keep alive connections on server
- `keepalive_time 30m` - set max time of keep-alive request processing to 30 minutes
- `keepalive_requests` - maximum number of requests inside single keep-alive connection
- `keepalive_disable msie6` - disable keep-alive connections processing for IE6

group: keepalive


