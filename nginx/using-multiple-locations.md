# Using multiple locations

```nginx
server {
  location /images {
    # ...
  }

  location ~* \.(png|jpg|gif)$ {
    # ...
  }
}
```

- `server {` - virtual server configuration block
- `location /images` - standard location to process all requests starting with `/images`
- `location ~* \.(png|jpg|gif)$` - second location that uses regex

group: location


