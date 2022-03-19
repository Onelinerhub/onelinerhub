# How to gzip content

```nginx
server {
  gzip on;
  gzip_vary on;
  gzip_min_length 1024;
  gzip_comp_level 8;
  gzip_types text/plain text/css text/xml text/javascript; 
}
```

- `server {` - virtual server configuration block
- `gzip on` - enable gzip compression
- `gzip_vary on` - enables `Vary: Accept-Encoding` response header
- `gzip_min_length 1024` - Nginx will not gzip responses less than 1024 bytes (because it's not efficient)
- `gzip_comp_level 8` - set compression level to `8` (out of `9`, where `9` is strongest compression)
- `gzip_types` - list mime types to enable gzip for


