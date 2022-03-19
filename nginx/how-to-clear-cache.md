# How to clear cache

```nginx
proxy_cache_path /var/cache/nginx levels=2:2:2 keys_zone=my_cache:100m max_size=50g inactive=60m use_temp_path=off;

server {
  location / {
    proxy_cache my_cache;
    proxy_pass http://backend;
  }
}
```

- `proxy_cache_path` - setup proxy caching parameters
- `/var/cache/nginx` - folder to store cache (make sure it's available for writing to Nginx)
- `levels=2:2:2` - cache files will be saved into 3 levels of 2 chars directories (to optimize file access on disk)
- `keys_zone=` - setup key zone params
- `my_cache` - name of cache key zone
- `100m` - key names storage (100m will allow storing approximately 1 million key names)
- `max_size=50g` - set maximum size of cache storage to 50G
- `inactive=60m` - delete cached data if it's not being access for 60 minutes
- `use_temp_path=off` - optimize cache writing by skipping temporary usage
- `proxy_cache my_cache` - set configured cache zone to use for caching this proxy upstream
- `proxy_pass http://backend` - sample proxy upstream

group: cache


