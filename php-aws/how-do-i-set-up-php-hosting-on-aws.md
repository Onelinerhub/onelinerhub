# How do I set up PHP hosting on AWS?
// plain

Setting up PHP hosting on AWS requires a few steps. First, create an Amazon EC2 instance with the Amazon Linux AMI. Then, install Apache web server, MySQL, and PHP using the `yum` package manager. The following code block shows an example of this:

```
$ sudo yum install httpd mysql php
```

Once the installation is completed, configure Apache to use the PHP module and restart the Apache web server. The following code block shows an example of this:

```
$ sudo a2enmod php7.2
$ sudo systemctl restart httpd
```

Once Apache is running, create a MySQL database and user with permissions to access the database. Then, create your PHP application and upload it to the server. Finally, configure your domain name to point to the server.

## Code explanation

1. `yum install httpd mysql php`: Installs Apache web server, MySQL, and PHP using the `yum` package manager.
2. `a2enmod php7.2`: Enables the PHP module on Apache.
3. `systemctl restart httpd`: Restarts the Apache web server.

## Helpful links
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Amazon Linux AMI](https://aws.amazon.com/amazon-linux-ami/)
- [Apache HTTP Server](https://httpd.apache.org/)
- [MySQL](https://www.mysql.com/)
- [PHP](https://www.php.net/)

onelinerhub: [How do I set up PHP hosting on AWS?](https://onelinerhub.com/php-aws/how-do-i-set-up-php-hosting-on-aws)