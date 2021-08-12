# Creating SSL certificate for Nginx

Make sure to [install Certbot](https://onelinerhub.com/certbot/install_certbot_on_ubuntu) and [Certbot Nginx plugin](https://onelinerhub.com/certbot/install_nginx_plugin_for_certbot_on_ubuntu).

```bash
certbot --nginx
```

- certbot - main certbot executable
- --nginx - will parse Nginx configs and ask which hosts to add SSLs to
