# How do I install PHP on an Amazon EC2 instance?
// plain

1. First, launch an Amazon EC2 instance with a supported Amazon Machine Image (AMI).
2. Connect to the instance with SSH.
3. Install Apache web server and PHP packages on the instance:
   ```
   sudo yum install httpd24 php56
   ```
4. Start the Apache web server:
   ```
   sudo service httpd start
   ```
5. Test the installation by creating a PHP file:
   ```
   sudo vi /var/www/html/test.php
   ```
   Add the following lines to the file:
   ```
   <?php
   phpinfo();
   ?>
   ```
6. Save the file and open it in a browser to view the output of the `phpinfo()` function.
7. Finally, configure the security group of the instance to allow incoming traffic on port 80.

## Helpful links

- [Amazon EC2 Documentation](https://aws.amazon.com/documentation/ec2/)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [PHP Documentation](https://www.php.net/docs.php)

onelinerhub: [How do I install PHP on an Amazon EC2 instance?](https://onelinerhub.com/php-aws/how-do-i-install-php-on-an-amazon-ec--instance)