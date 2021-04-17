# Redirect HTTP to HTTPS (non-SSL to SSL)

```nginx
server {
  server_name  domain.com;
  return       301 https://$server_name$request_uri;
}
```
