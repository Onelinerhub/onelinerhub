# Redirect www to non-www

Replace ```domain.com``` with your domain.

```nginx
server {
  server_name  www.domain.com;
  return       301 http://domain.com$request_uri;
}
```
