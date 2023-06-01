# How do I install and configure php-mbstring on an AWS EC2 instance?
// plain

To install and configure php-mbstring on an AWS EC2 instance, follow these steps:

1. Connect to your EC2 instance using SSH.
2. Install php-mbstring by running the following command:

```
sudo yum install php-mbstring
```

3. To enable mbstring, edit the `/etc/php.ini` file and add the following line:

```
extension=mbstring
```

4. Restart your web server to apply the changes.

```
sudo service httpd restart
```

5. To verify the installation, run the following command:

```
php -m | grep mbstring
```

The output should look like this:

```
mbstring
```

6. Finally, test your setup by running a PHP script that uses the mbstring library.

## Helpful links
- [How to Install PHP on Amazon Linux](https://docs.aws.amazon.com/aws-technical-content/latest/aws-linux-install-php/index.html)
- [How to Configure PHP on Amazon Linux](https://docs.aws.amazon.com/aws-technical-content/latest/aws-linux-configure-php/index.html)

onelinerhub: [How do I install and configure php-mbstring on an AWS EC2 instance?](https://onelinerhub.com/php-aws/how-do-i-install-and-configure-php-mbstring-on-an-aws-ec--instance)