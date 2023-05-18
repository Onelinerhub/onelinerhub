# How to configure Nginx for WordPress?
// plain

1. Install Nginx and PHP on your server.
2. Create a new Nginx configuration file for your WordPress site.
```
server {
    listen 80;
    server_name example.com;
    root /var/www/example.com;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
    }
}
```
3. Enable the new configuration file and restart Nginx.
```
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```
4. Install WordPress on your server.
5. Configure WordPress to use the Nginx configuration.

## Helpful links
- [How To Install Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
- [How To Install WordPress with Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-nginx-on-ubuntu-18-04)

onelinerhub: [How to configure Nginx for WordPress?](https://onelinerhub.com/php-wordpress/how-to-configure-nginx-for-wordpress)