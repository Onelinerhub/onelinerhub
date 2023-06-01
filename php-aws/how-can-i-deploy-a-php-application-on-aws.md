# How can I deploy a PHP application on AWS?
// plain

Deploying a PHP application on AWS can be done in several steps.

1. Create an AWS account and log in to the AWS Management Console.
2. Create an EC2 instance.
3. Connect to the instance using SSH.
4. Install the Apache web server and PHP.
5. Configure the web server to serve the application.
6. Upload the application code to the instance.
7. Access the application using the instance's public DNS address.

For example, to install Apache and PHP on an Ubuntu EC2 instance, the code below can be used.
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install php libapache2-mod-php
```
## Output example

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  apache2-bin apache2-data libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libaprutil1-ldap liblua5.2-0 ssl-cert
Suggested packages:
  apache2-doc apache2-suexec-pristine apache2-suexec-custom
  libapache2-mod-macro
The following NEW packages will be installed:
  apache2 libapache2-mod-php libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libaprutil1-ldap liblua5.2-0 php ssl-cert
0 upgraded, 9 newly installed, 0 to remove and 0 not upgraded.
Need to get 6,065 kB of archives.
After this operation, 21.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

## Helpful links
* [AWS EC2 Documentation](https://aws.amazon.com/documentation/ec2/)
* [Apache Installation Guide](https://httpd.apache.org/docs/2.4/install.html)
* [PHP Installation Guide](https://www.php.net/manual/en/install.php)

onelinerhub: [How can I deploy a PHP application on AWS?](https://onelinerhub.com/php-aws/how-can-i-deploy-a-php-application-on-aws)