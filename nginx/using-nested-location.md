# Using nested locations

```nginx
server {
  location /images {
    location /images/icons {
      # ...
    }
    
    location /images/photos {
      # ...
    }
  }
}
```

- `server {` - virtual server configuration block
- `location /images {` - parent location block that matches requests starting with `/images`
- `location /images/icons` - nested location that matches `/images/icons`
- `location /images/photos` - nested location that matches `/images/photos`

group: location


