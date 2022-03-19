# Using internal redirects

### This example is based on backend which should return `x-accel-redirect` header when it needs Nginx to access `/hidden/` location:

```nginx
server {
  listen 80;

  location / {
    proxy_pass http://backend;
  }

  location /hidden/ {
    internal;
    root /path/to/hidden;
  }
}
```

- `server {` - virtual server configuration block
- `proxy_pass http://backend` - sample proxy to some backend that should return `x-accel-redirect` header
- `location /hidden/` - location block for internal redirect
- `internal` - make sure this location can not be accessed publicly, but only using internal redirect
- `root /path/to/hidden` - change root to other directory to access needed files (just an example)


