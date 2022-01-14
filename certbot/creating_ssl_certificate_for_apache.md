# Creating SSL certificate for Apache

```bash
certbot --apache
systemctl reload apache2
```

- `--apache` - automatically configure ceritifcates for available Apache hosts
- `reload apache2` - restart Apache webserver after certificates installation is complete


link_youtube: https://youtu.be/8CJfOwWISy0
