# Redirect www to non-www

```nginx
server {
  server_name  www.domain.com;
  return       301 http://domain.com$request_uri;
}
```

- www.domain.com - www-included domain name
- 301 - redirect code type (permanent redirect)
