# How to configure PHP-FPM and Nginx in Symfony?
// plain

1. Install and configure Nginx and PHP-FPM:
   - Install Nginx and PHP-FPM packages on your system.
   - Configure Nginx to use PHP-FPM as the FastCGI processor.
   - Configure Nginx to serve the Symfony application.

2. Configure Symfony to use Nginx and PHP-FPM:
   - Add the following configuration to your `config/packages/framework.yaml` file:
   ```
   framework:
       php_errors:
           log: true
           log_level: 'error'
           log_max_files: 10
   ```
   - Add the following configuration to your `config/packages/web_server.yaml` file:
   ```
   web_server:
       php_fpm:
           enabled: true
           host: '127.0.0.1'
           port: 9000
   ```

3. Restart Nginx and PHP-FPM services:
   - Restart Nginx and PHP-FPM services to apply the changes.

4. Test the configuration:
   - Access your Symfony application in the browser and check the output.

5. ## Helpful links
   - [Nginx Installation Guide](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/)
   - [PHP-FPM Installation Guide](https://www.php.net/manual/en/install.fpm.php)
   - [Symfony Configuration Reference](https://symfony.com/doc/current/reference/configuration.html)

onelinerhub: [How to configure PHP-FPM and Nginx in Symfony?](https://onelinerhub.com/php-symfony/how-to-configure-php-fpm-and-nginx-in-symfony)