# Enable client cache

```nginx
server {
  location ~* \.(css|js|png|jpg|gif|svg)$ {
    expires 30d;
    add_header Cache-Control "public";
  }
}
```

- `server {` - virtual server configuration block
- `css|js|png|jpg|gif|svg` - files extensions to enable client caching for
- `expires 30d` - cache content in browser for 30 days
- `add_header` - sets specified header
- `Cache-Control "public"` - special header to ask browsers to cache specified content

group: client_cache


