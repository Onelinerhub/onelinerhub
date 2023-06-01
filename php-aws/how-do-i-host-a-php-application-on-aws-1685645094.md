# How do I host a PHP application on AWS?
// plain

1. Sign up for an AWS account and create an EC2 instance.
2. Connect to the EC2 instance using SSH.
3. Install Apache, MySQL, and PHP on the EC2 instance.
4. Configure Apache and MySQL.
5. Upload your PHP application to the EC2 instance.
6. Configure the application to use the MySQL database.
7. Test the application in a web browser.

Example code to install Apache, MySQL, and PHP on the EC2 instance:

```
sudo yum install httpd24 php56 mysql55-server php56-mysqlnd
```

## Output example


```
Loaded plugins: priorities, update-motd, upgrade-helper
amzn-main/latest                                                                                                                                                           | 2.1 kB  00:00:00
amzn-updates/latest                                                                                                                                                        | 2.3 kB  00:00:00
Resolving Dependencies
--> Running transaction check
---> Package httpd24.x86_64 0:2.4.37-1.82.amzn1 will be installed
---> Package mysql55-server.x86_64 0:5.5.62-1.23.amzn1 will be installed
---> Package php56.x86_64 0:5.6.40-1.28.amzn1 will be installed
---> Package php56-mysqlnd.x86_64 0:5.6.40-1.28.amzn1 will be installed
```

## Code explanation


* sudo yum install - install the packages listed
* httpd24 - Apache web server
* php56 - PHP language
* mysql55-server - MySQL database server
* php56-mysqlnd - MySQL database client library for PHP

## Helpful links

* [Amazon EC2](https://aws.amazon.com/ec2/)
* [Apache HTTP Server](https://httpd.apache.org/)
* [MySQL](https://www.mysql.com/)
* [PHP](https://www.php.net/)

onelinerhub: [How do I host a PHP application on AWS?](https://onelinerhub.com/php-aws/how-do-i-host-a-php-application-on-aws-1685645094)