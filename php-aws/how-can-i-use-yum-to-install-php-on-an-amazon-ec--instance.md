# How can I use Yum to install PHP on an Amazon EC2 instance?
// plain

Yum is a package manager for Linux distributions that can be used to install PHP on an Amazon EC2 instance. The following steps can be used to install PHP on an Amazon EC2 instance using Yum:

1. Update the Yum package manager:
```
sudo yum update
```

2. Install the PHP packages:
```
sudo yum install php php-mysql
```

3. Verify the installation by running the following command:
```
php -v
```

## Output example

```
PHP 7.2.34 (cli) (built: Mar 24 2020 11:01:37) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```

4. Configure the PHP settings:
```
sudo vi /etc/php.ini
```

5. Restart the Apache web server:
```
sudo service httpd restart
```

6. Test the PHP installation by creating a PHP info page:
```
sudo vi /var/www/html/info.php
```

7. Test the page by visiting the URL in a web browser:
```
http://<ec2-instance-ip>/info.php
```

## Helpful links
- [Yum Documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-yum)
- [Installing PHP on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)

onelinerhub: [How can I use Yum to install PHP on an Amazon EC2 instance?](https://onelinerhub.com/php-aws/how-can-i-use-yum-to-install-php-on-an-amazon-ec--instance)