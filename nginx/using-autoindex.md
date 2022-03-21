# Using autoindex

```nginx
server {
  location /files/ {
    autoindex on;
  }
}
```

- `server {` - virtual server configuration block
- `location /files/ {` - location will be triggered on all `/files/...` requests
- `autoindex on` - enabled automatic directories and files listing from web


