# Redirect www to non-www in Nginx

Replace ```domain.com``` with your domain.

```nginx
server {
  server_name  www.domain.com;
  return       301 http://domain.com$request_uri;
}
```
