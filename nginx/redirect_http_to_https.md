# Redirect HTTP to HTTPS (non-SSL to SSL)

```nginx
server {
  server_name  domain.com;
  return       301 https://$server_name$request_uri;
}
```

- domain.com - your host domain name
- 301 - this will trigger 301-type redirect (moved permanently).
