# Using x-xss-protection header

```nginx
server {
  add_header X-XSS-Protection "1; mode=block";
}
```

- `server {` - virtual server configuration block
- `add_header` - sets specified header
- `X-XSS-Protection` - controls if XSS protection should be additionally enabled/disabled in browser
- `1; mode=block` - enables browser XSS check and ensures insecure pages will not be loaded


