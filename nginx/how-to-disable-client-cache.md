# How to disable client cache

```nginx
server {
  location ~* \.(css|js|png|jpg|gif|svg)$ {
    add_header Cache-Control 'no-store, no-cache';
    add_header Last-Modified $date_gmt;
    if_modified_since off;
    expires off;
  }
}
```

- `server {` - virtual server configuration block
- `css|js|png|jpg|gif|svg` - files extensions to disable client caching for
- `add_header` - sets specified header
- `Cache-Control 'no-store, no-cache'` - ask browsers to disable content cache
- `Last-Modified $date_gmt` - set last modified to current time to make sure browsers will ask for latest versions
- `expires off` - disable cache expiration header
- `if_modified_since off` - disables check for document modification (which doesn't return document if it's not modified - we don't need this)

group: client_cache


