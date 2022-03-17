# Set access-control-allow-origin header

```nginx
server {
  add_header "Access-Control-Allow-Origin" "example.org";
}
```

- `server {` - virtual server configuration block
- `add_header` - sets specified header
- `Access-Control-Allow-Origin` - set CORS header to control access from origins
- `example.org` - sample origin to allow

group: cors


