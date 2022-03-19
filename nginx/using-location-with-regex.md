# Using location with regex

```nginx
server {
  location ~* \.(png|jpg|gif)$ {
    # ...
  }
}
```

- `server {` - virtual server configuration block
- `location` - location block start
- `~*` - use regex in this location block
- `\.(png|jpg|gif)$` - sample regex to use (match image extensions)

group: location


