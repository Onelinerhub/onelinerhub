# Setup HTTP/2 with Nginx

```nginx
server {
  listen 443 ssl http2;
  server_name example.org;
  
  ssl_certificate /path/to/domain.crt;
  ssl_certificate_key /path/to/pdomain.key;
  
  ssl_protocols TLSv1.2;
}
```

- `http2` - enable HTTP/2 protocol (used with SSL only)
- `example.org` - example server name
- `/path/to/domain.crt` - path to SSL certificate file
- `/path/to/pdomain.key` - path to SSL key file


