# How do I deploy a PHP website on AWS?
// plain

1. Create an AWS account and sign up for an Amazon Web Services (AWS) account.
2. Create an Amazon Elastic Compute Cloud (EC2) instance.
3. Connect to the EC2 instance using an SSH client.
4. Install the Apache web server and PHP on the EC2 instance.
5. Configure Apache to serve your website.
6. Upload your website files to the EC2 instance.
7. Test your website.

Example code block:
```
# Install Apache web server
sudo apt-get install apache2

# Install PHP
sudo apt-get install php

# Configure Apache to serve your website
sudo nano /etc/apache2/sites-available/000-default.conf
```

## Output example

```
<VirtualHost *:80>
    ServerName example.com

    DocumentRoot /var/www/html
    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

## Code explanation

- `sudo apt-get install apache2` - This command installs the Apache web server on the EC2 instance.
- `sudo apt-get install php` - This command installs PHP on the EC2 instance.
- `sudo nano /etc/apache2/sites-available/000-default.conf` - This command opens the Apache configuration file in the nano text editor.

## Helpful links
- [AWS Documentation: Getting Started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [PHP Documentation](https://www.php.net/docs.php)

onelinerhub: [How do I deploy a PHP website on AWS?](https://onelinerhub.com/php-aws/how-do-i-deploy-a-php-website-on-aws)