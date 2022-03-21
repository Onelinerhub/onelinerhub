# Using x-frame-options header

```nginx
server {
  add_header X-Frame-Options "SAMEORIGIN";
}
```

- `server {` - virtual server configuration block
- `add_header` - sets specified header
- `X-Frame-Options` - this header controls loading of our website in iframes 
- `SAMEORIGIN` - ensure our website can be loaded inside iframe from our domain only (from same origin)


