# Using open_file_cache to optimize file access

```nginx
server {
  open_file_cache max=100000 inactive=30m;
  open_file_cache_valid 5m;
  open_file_cache_min_uses 2;
  open_file_cache_errors on;
}
```

- `server {` - virtual server configuration block
- `max=100000` - cache up to 100000 file descriptors
- `inactive=30m` - if file is accessed 2 times within 30 minutes, we will cache it's descriptor
- `open_file_cache_valid` - period of time to check if file is updated
- `open_file_cache_min_uses` - min number of times file is accessed within 30 minutes (`inactive` param) to cache it's descriptor
- `open_file_cache_errors` - also cache errors like absent file or access denied


