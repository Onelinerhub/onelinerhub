# How do I configure Nginx for Laravel using PHP?
// plain

To configure Nginx for Laravel using PHP, follow the steps below:

1. Create a server block in your `/etc/nginx/sites-available` directory. Below is an example of a server block for a Laravel application:
```
server {
    listen 80;
    server_name example.com;
    root /var/www/example.com/public;

    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri /index.php =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```
2. Activate the server block by creating a symbolic link from the `sites-available` directory to the `sites-enabled` directory:
```
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```
3. Test the Nginx configuration for syntax errors:
```
sudo nginx -t
```
4. If the test is successful, restart Nginx to apply the changes:
```
sudo systemctl restart nginx
```

The above steps should configure Nginx for Laravel using PHP.

## Helpful links
- [Configure Nginx for Laravel](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-laravel-with-nginx-on-ubuntu-18-04)
- [Nginx Server Blocks](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)

onelinerhub: [How do I configure Nginx for Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-configure-nginx-for-laravel-using-php)