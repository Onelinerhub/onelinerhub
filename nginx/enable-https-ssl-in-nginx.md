# Enable HTTPS (SSL) in Nginx

```nginx
server {
  listen 443 ssl;
  server_name example.org;
  
  ssl_certificate /etc/nginx/certificate/example.crt;
  ssl_certificate_key /etc/nginx/certificate/example.key;
}
```

- `server {` - virtual server configuration block
- `listen 443 ssl` - enable SSL
- `example.org` - example server name to enable HTTPs for
- `/etc/nginx/certificate/example.crt` - path to SSL certificate file
- `/etc/nginx/certificate/example.key` - path to SSL key file


