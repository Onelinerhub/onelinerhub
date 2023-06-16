# How can I configure Nginx to work with Laravel on a PHP server?
// plain

You can configure Nginx to work with Laravel on a PHP server by following the steps below:

1. Install Nginx and PHP-FPM:

```bash
sudo apt-get install nginx php-fpm
```

2. Create a new Nginx configuration file in the `/etc/nginx/sites-available` directory. This file should contain the following:

```
server {
    listen 80;
    server_name example.com;
    root /var/www/example.com/public;

    index index.html index.htm index.php;

    charset utf-8;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location = /favicon.ico { access_log off; log_not_found off; }
    location = /robots.txt  { access_log off; log_not_found off; }

    access_log off;
    error_log  /var/log/nginx/example.com-error.log error;

    sendfile off;

    client_max_body_size 100m;

    location ~ \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_intercept_errors off;
        fastcgi_buffer_size 16k;
        fastcgi_buffers 4 16k;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

3. Enable the new configuration file by creating a symbolic link from the `/etc/nginx/sites-enabled` directory to the configuration file in the `/etc/nginx/sites-available` directory.

```bash
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com
```

4. Test the configuration file for syntax errors.

```bash
sudo nginx -t
```

5. Restart Nginx to apply the changes.

```bash
sudo service nginx restart
```

6. Install the Laravel framework and configure the web server.

7. Test your Laravel application by navigating to the URL in your web browser.

For more information, please refer to the following links:
- [How to Install and Configure Laravel with LEMP on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-laravel-with-lemp-on-ubuntu-18-04)
- [How To Install Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
- [How To Configure Nginx as a Web Server and Reverse Proxy for Apache on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-as-a-web-server-and-reverse-proxy-for-apache-on-ubuntu-18-04)

onelinerhub: [How can I configure Nginx to work with Laravel on a PHP server?](https://onelinerhub.com/php-laravel/how-can-i-configure-nginx-to-work-with-laravel-on-a-php-server)