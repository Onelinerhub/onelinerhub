# Serving multiple hosts with server_name

```nginx
server {
  server_name domain1.com domain2.com;
  # ...
}
```

- `server {` - virtual server configuration block
- `server_name` - host name to handle requests for
- `domain1.com` - first domain to serve
- `domain2.com` - second domain to serve


