# How do I set up a PHP server on AWS?
// plain

1. Create an AWS account and sign in to the AWS Management Console.
2. Choose the EC2 service from the list of all services.
3. Select the region in which you want to launch your instance.
4. Select the Amazon Machine Image (AMI) that you want to use. For PHP, choose an AMI with either Apache or Nginx installed.
5. Choose an instance type.
6. Configure the instance details.
7. Launch the instance and connect to it using SSH.

```
# To install PHP
sudo apt-get update
sudo apt-get install php
```

## Output example

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libapache2-mod-php
Suggested packages:
  php-pear
The following NEW packages will be installed:
  libapache2-mod-php php
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/2,742 kB of archives.
After this operation, 10.7 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
```

Parts of code:
- `sudo apt-get update`: This command updates the list of available packages and their versions.
- `sudo apt-get install php`: This command installs the PHP package on the server.

## Helpful links
- [AWS EC2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [How to Install PHP on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)

onelinerhub: [How do I set up a PHP server on AWS?](https://onelinerhub.com/php-aws/how-do-i-set-up-a-php-server-on-aws)