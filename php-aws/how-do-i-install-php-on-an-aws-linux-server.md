# How do I install PHP on an AWS Linux server?
// plain

1. Log into the AWS Linux server as the root user.
2. Run the command `yum install php` to install PHP on the server.
3. Run the command `yum install php-mysql` to install the MySQL module for PHP.
4. Run the command `yum install php-gd` to install the GD library for PHP.
5. Run the command `yum install php-cli` to install the command line interface for PHP.
6. Run the command `yum install php-pear` to install the PEAR package manager for PHP.
7. Run the command `service httpd restart` to restart the Apache web server.

Example code block:
```
yum install php php-mysql php-gd php-cli php-pear
service httpd restart
```

## Output example

```
Loaded plugins: priorities, update-motd, upgrade-helper
Resolving Dependencies
--> Running transaction check
---> Package php.x86_64 0:5.4.16-42.el7 will be installed
---> Package php-cli.x86_64 0:5.4.16-42.el7 will be installed
---> Package php-common.x86_64 0:5.4.16-42.el7 will be installed
---> Package php-gd.x86_64 0:5.4.16-42.el7 will be installed
---> Package php-mysql.x86_64 0:5.4.16-42.el7 will be installed
---> Package php-pear.noarch 1:1.10.1-6.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                  Arch               Version                  Repository
                                                                            Size
================================================================================
Installing:
 php                     x86_64             5.4.16-42.el7            base     4.3 M
 php-cli                 x86_64             5.4.16-42.el7            base    11 M
 php-common              x86_64             5.4.16-42.el7            base    74 k
 php-gd                  x86_64             5.4.16-42.el7            base    58 k
 php-mysql               x86_64             5.4.16-42.el7            base    86 k
 php-pear                noarch             1.10.1-6.el7             base    1.4 M

Transaction Summary
================================================================================
Install  6 Packages

Total download size: 17 M
Installed size: 62 M
Is this ok [y/d/N]: y
Downloading packages:
(1/6): php-5.4.16-42.el7.x86_64.rpm                                          | 4.3 MB   00:00
(2/6): php-cli-5.4.16-42.el7.x86_64.rpm                                     | 11 MB    00:00
(3/6): php-common-5.4.16-42.el7.x86_64.rpm                                  |  74 kB   00:00
(4/6): php-gd-5.4.16-42.el7.x86_64.rpm                                      |  58 kB   00:00
(5/6): php-mysql-5.4.16-42.el7.x86_64.rpm                                   |  86 kB   00:00
(6/6): php-pear-1.10.1-6.el7.noarch.rpm                                     | 1.4 MB   00:00
--------------------------------------------------------------------------------
Total                                                                 7.3 MB/s |  17 MB  00:02
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : php-cli-5.4.16-42.el7.x86_64                                  1/6
  Installing : php-common-5.4.16-42.el7.x86_64                               2/6
  Installing : php-5.4.16-42.el7.x86_64                                     3/6
  Installing : php-gd-5.4.16-42.el7.x86_64                                   4/6
  Installing : php-mysql-5.4.16-42.el7.x86_64                                5/6
  Installing : php-pear-1.10.1-6.el7.noarch                                  6/6
  Verifying  : php-pear-1.10.1-6.el7.noarch                                  1/6
  Verifying  : php-mysql-5.4.16-42.el7.x86_64                                2/6
  Verifying  : php-gd-5.4.16-42.el7.x86_64                                   3/6
  Verifying  : php-5.4.16-42.el7.x86_64                                     4/6
  Verifying  : php-cli-5.4.16-42.el7.x86_64                                  5/6
  Verifying  : php-common-5.4.16-42.el7.x86_64                               6/6

Installed:
  php.x86_64 0:5.4.16-42.el7                                                php-cli.x86_64 0:5.4.16-42.el7                                               php-common.x86_64 0:5.4.16-42.el7                                            php-gd.x86_64 0:5.4.16-42.el7                                                php-mysql.x86_64 0:5.4.16-42.el7                                             php-pear.noarch 1:1.10.1-6.el7

Complete!
[root@ip-172-31-33-25 ~]# service httpd restart
Redirecting to /bin/systemctl restart  httpd.service
```

## Helpful links
- [AWS Documentation - Install PHP on an Amazon Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html)
- [DigitalOcean - How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Amazon Linux](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-amazon-linux)

onelinerhub: [How do I install PHP on an AWS Linux server?](https://onelinerhub.com/php-aws/how-do-i-install-php-on-an-aws-linux-server)