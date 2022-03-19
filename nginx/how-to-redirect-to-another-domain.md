# How to redirect to another domain

```nginx
server {
  rewrite ^/(old.*)$ https://domain.com/$1 redirect;
}
```

- `server {` - virtual server configuration block
- `rewrite` - define URL rewrite rule
- `^/(old.*)$` - regex to match urls to redirect
- `domain.com` - new domain to redirect to
- `redirect` - ask Nginx to do a real redirect instead of silent rewrite

group: redirect


