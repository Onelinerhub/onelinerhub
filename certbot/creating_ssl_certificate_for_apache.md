# Creating SSL certificate for Apache

Make sure to [install Certbot](https://onelinerhub.com/certbot/install_certbot_on_ubuntu) and [Certbot Apache plugin](/certbot/install_certbot_apache_plugin_on_ubuntu).

```bash
certbot --apache
systemctl reload apache2
```

- --apache - automatically configure ceritifcates for available Apache hosts
- reload apache2 - restart Apache webserver after certificates installation is complete
