# How to use Nginx Redis caching

```nginx
server {
  location / {
    set $redis_key $uri;

    redis_pass 127.0.0.1:6379;
    default_type text/html;
    error_page 404 = /fallback;
  }

  location = /fallback {
      proxy_pass backend;
  }
}
```

- `$redis_key` - name of the caching key ([Nginx Redis](https://www.nginx.com/resources/wiki/modules/redis/) should be used)
- `$uri` - use URL path as a caching key
- `redis_pass 127.0.0.1:6379` - connection parameters for Redis server
- `error_page 404` - handle situations when key is not in the cache (not found in Redis)
- `/fallback` - internal location to generate pages from real backend (instead of cache)


