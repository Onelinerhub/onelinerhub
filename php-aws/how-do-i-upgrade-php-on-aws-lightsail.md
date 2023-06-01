# How do I upgrade PHP on AWS Lightsail?
// plain

**Upgrading PHP on AWS Lightsail**

1. Log into your AWS Lightsail account and select the instance you wish to upgrade.
2. Select the "Networking" tab and then select "Create static IP".
3. Select the "Manage" tab and then select "Connect using SSH".
4. Enter the following command to update the package index:
```
sudo apt-get update
```
5. Install the latest version of PHP using the following command:
```
sudo apt-get install php7.2
```
6. Verify the installation by running the following command:
```
php -v

## Output example

PHP 7.2.x (cli) (built: Sep xxxx xx xx:xx:xx) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```
7. Restart Apache for the changes to take effect:
```
sudo service apache2 restart
```

## Helpful links
- [AWS Lightsail Documentation](https://lightsail.aws.amazon.com/ls/docs)
- [How to Upgrade PHP on Ubuntu](https://www.rosehosting.com/blog/how-to-upgrade-php-on-ubuntu/)

onelinerhub: [How do I upgrade PHP on AWS Lightsail?](https://onelinerhub.com/php-aws/how-do-i-upgrade-php-on-aws-lightsail)