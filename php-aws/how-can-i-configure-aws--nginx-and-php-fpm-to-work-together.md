# How can I configure AWS, Nginx and PHP-FPM to work together?
// plain

1. Install Nginx and PHP-FPM on the AWS EC2 instance.
2. Create a new Nginx configuration file for your website.
   ```
   server {
       listen 80;
       server_name www.example.com;
       root /var/www/html;
       index index.php index.html;
   }
   ```
3. Add the following lines to the configuration file to enable PHP-FPM:
   ```
   location ~ \.php$ {
       include fastcgi_params;
       fastcgi_pass 127.0.0.1:9000;
       fastcgi_index index.php;
       fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
   }
   ```
4. Start Nginx and PHP-FPM services:
   ```
   sudo service nginx start
   sudo service php-fpm start
   ```
5. Test if the configuration is working by creating a `phpinfo.php` file in the `/var/www/html` directory with the following content:
   ```
   <?php
   phpinfo();
   ?>
   ```
6. Access the file in a browser and view the output:
   ```
   PHP Version 7.2.34
   ```
7. If everything is working correctly, you can now deploy your website.

## Helpful links
- [How to Install Nginx and PHP-FPM on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
- [Configuring Nginx and PHP-FPM for Optimal Performance](https://www.digitalocean.com/community/tutorials/configuring-nginx-and-php-fpm-for-optimal-performance)

onelinerhub: [How can I configure AWS, Nginx and PHP-FPM to work together?](https://onelinerhub.com/php-aws/how-can-i-configure-aws--nginx-and-php-fpm-to-work-together)