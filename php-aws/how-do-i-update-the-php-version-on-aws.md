# How do I update the PHP version on AWS?
// plain

Updating the PHP version on AWS can be done by following these steps:

1. First, you need to log in to your AWS EC2 instance.
2. Once logged in, you need to check the current version of PHP installed on the instance. To do this, you can run the following command in the terminal:
```
php -v
```
This will output the version of PHP installed on the instance.
3. Next, you need to update the PHP version by running the following command in the terminal:
```
sudo yum update php
```
This will update the installed version of PHP on the instance.
4. After the update is finished, you can verify the updated version of PHP by running the same command as before:
```
php -v
```
This will output the updated version of PHP installed on the instance.
5. Finally, you need to restart the web server for the changes to take effect. To do this, you can run the following command in the terminal:
```
sudo service httpd restart
```

This will restart the web server and the new version of PHP will be running on the instance.

## Helpful links
- [AWS EC2 Documentation](https://aws.amazon.com/ec2/)
- [PHP Documentation](https://www.php.net/manual/en/index.php)

onelinerhub: [How do I update the PHP version on AWS?](https://onelinerhub.com/php-aws/how-do-i-update-the-php-version-on-aws)