# Nginx config example

### This is a full config example, usually available under `/etc/nginx/nginx.conf`:

```nginx
user www-data www-data;

http {
  include conf/mime.types;
  default_type application/octet-stream;

  server {
    listen 80;
    server_name domain.com;
    root /var/www/domain;
    index index.html;
  }
}
```

- `user www-data www-data` - user/group to run Nginx from
- `http {` - main Nginx HTTP server configuration block
- `server {` - virtual server configuration block
- `listen 80` - listen to 80 port (standard HTTP protocol)
- `server_name` - host name to handle requests for
- `/var/www/domain` - path to server files/scripts from
- `index.html` - default file to serve (for `/` requests)


