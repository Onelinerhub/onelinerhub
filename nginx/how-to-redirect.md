# How to redirect

```nginx
server {
  rewrite ^/old$ /new redirect; 
}
```

- `server {` - virtual server configuration block
- `rewrite` - define URL rewrite rule
- `^/old$` - regex to match urls to redirect
- `/new` - new url to redirect to
- `redirect` - ask Nginx to do a real redirect instead of silent rewrite

group: redirect


