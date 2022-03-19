# How to disable data caching in Nginx

```nginx
server {
  location / {
    # proxy_cache my_cache;
    proxy_pass http://backend;
  }
}
```

- `server {` - virtual server configuration block
- `proxy_cache my_cache` - remove or connect this directive to disable upstream caching

group: cache


