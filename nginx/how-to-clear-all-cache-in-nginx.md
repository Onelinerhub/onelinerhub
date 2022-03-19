# How to clear all cache in Nginx

### Before clearing cache make sure to [disable caching](/nginx/how-to-disable-data-caching-in-nginx):

```bash
rm -rf /var/cache/nginx/*
nginx -s reload
```

- `rm -rf` - remove all files and folders recursively
- `/var/cache/nginx` - path to Nginx cache storage, configured in [cache settings](/nginx/how-to-clear-cache)
- `nginx -s reload` - reload Nginx after clearing cache

group: cache


