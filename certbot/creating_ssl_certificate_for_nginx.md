# Creating SSL certificate for Nginx

Make sure to [install Certbot]() and [Certbot Nginx plugin]().

```bash
certbot --nginx
```

- certbot - main certbot executable
- --nginx - will parse Nginx configs and ask which hosts to add SSLs to
