# How can I configure a PHP application to run on an EC2 instance using Nginx?
// plain

1. Install Nginx and PHP on the EC2 instance:
   ```
   sudo apt-get update
   sudo apt-get install nginx
   sudo apt-get install php
   ```
2. Create a configuration file for Nginx:
   ```
   sudo nano /etc/nginx/sites-available/example.com
   ```
   * `server_name` - The domain name of the application.
   * `root` - The document root for the application.
   * `index` - The default page to be served when a directory is requested.
   * `location` - The directive to pass requests to the PHP interpreter.

   ```
   server {
       server_name example.com;
       root /var/www/example.com/public_html;
       index index.php index.html index.htm;
       location / {
           try_files $uri $uri/ =404;
       }
       location ~ \.php$ {
           include snippets/fastcgi-php.conf;
           fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
       }
   }
   ```

3. Enable the new configuration and restart Nginx:
   ```
   sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```
4. Create a PHP file to test the configuration:
   ```
   sudo nano /var/www/example.com/public_html/index.php
   ```
   ```
   <?php
       phpinfo();
   ?>
   ```
5. Visit the domain in a web browser to test the configuration:
   ```
   http://example.com
   ```
   Output:
   ```
   PHP Version 7.2.24-0ubuntu0.18.04.4
   ```

## Helpful links
1. [How To Install Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
2. [How To Install Linux, Nginx, MySQL, PHP (LEMP stack) in Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-18-04)
3. [How To Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx)

onelinerhub: [How can I configure a PHP application to run on an EC2 instance using Nginx?](https://onelinerhub.com/php-aws/how-can-i-configure-a-php-application-to-run-on-an-ec--instance-using-nginx)