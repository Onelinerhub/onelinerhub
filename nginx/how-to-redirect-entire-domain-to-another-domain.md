# How to redirect entire domain to another domain

```nginx
server {
  listen 80;
  server_name old.com;
  return 301 $scheme://new.com$request_uri;
}
```

- `server {` - virtual server configuration block
- `old.com` - current domain to redirect from
- `return 301` - use 301 redirect code
- `new.com` - new domain to redirect to
- `$scheme` - use same scheme for new domain (e.g. if `HTTPs` is used)
- `$request_uri` - use same URL for new domain

group: redirect


