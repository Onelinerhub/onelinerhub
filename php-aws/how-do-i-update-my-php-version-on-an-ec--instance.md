# How do I update my PHP version on an EC2 instance?
// plain

1. First, log into your EC2 instance using SSH.
2. Install the latest version of PHP using the command `sudo yum install php`.
3. Check the version of PHP installed using the command `php -v`.
4. If you need to update to a specific version of PHP, use the command `sudo yum update php-version`.
5. After updating PHP, check the version of PHP installed again using `php -v`.
6. Restart your web server using the command `sudo service httpd restart`.
7. Check the version of PHP in your web browser using the code `<?php phpinfo(); ?>`

```
<?php phpinfo(); ?>
```
## Output example

```
PHP Version 7.3.10
```

## Helpful links
* [How to Update PHP Version on EC2 Instance](https://www.cloudways.com/blog/update-php-version-on-aws-ec2-instance/)
* [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html)

onelinerhub: [How do I update my PHP version on an EC2 instance?](https://onelinerhub.com/php-aws/how-do-i-update-my-php-version-on-an-ec--instance)