# Enable and use Brotli

### Before configuring Brotli usage you need to install [Nginx Brotli module](https://docs.nginx.com/nginx/admin-guide/dynamic-modules/brotli/):

```nginx
server {
  brotli on;
  brotli_comp_level 6;
  brotli_static on;
  brotli_types text/plain text/css application/javascript application/json text/xml image/svg+xml;
}
```

- `brotli on` - enable Brotli module
- `brotli_comp_level` - specify compression level
- `brotli_static` - check if pre-compressed static files exist
- `brotli_types` - mime types to enable Brotli compression for


