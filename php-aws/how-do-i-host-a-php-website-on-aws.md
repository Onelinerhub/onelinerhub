# How do I host a PHP website on AWS?
// plain

1.  Create an AWS account and login to the AWS Management Console.
2.  Create an Amazon EC2 instance.
3.  Install Apache web server, PHP, and MySQL on the instance.
4.  Configure the Apache web server to recognize and serve PHP files.
5.  Create a MySQL database and user for your website.
6.  Upload your website files to the instance.
7.  Test your website.

Example code block:

```
sudo apt-get install apache2 php mysql-server
```

## Output example


```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  apache2-bin apache2-data libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libaprutil1-ldap libdb5.3 liblua5.1-0 libmcrypt4 mysql-client-5.7
  mysql-common mysql-server-5.7 php-common php-mysql php-pear
  php-readline
Suggested packages:
  www-browser apache2-doc apache2-suexec-pristine apache2-suexec-custom
  libterm-readline-gnu-perl libterm-readline-perl-perl php-doc
  php-pear-MDB2-Driver-mysql php-pear-MDB2-Driver-sqlite
  php-pear-MDB2-Driver-pgsql php-pear-MDB2-Driver-sqlite3
  php-pear-MDB2-Driver-oci8
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data libapr1 libaprutil1
  libaprutil1-dbd-sqlite3 libaprutil1-ldap libdb5.3 liblua5.1-0
  libmcrypt4 mysql-client-5.7 mysql-common mysql-server mysql-server-5.7
  php php-common php-mysql php-pear php-readline
0 upgraded, 17 newly installed, 0 to remove and 0 not upgraded.
Need to get 8,906 kB of archives.
After this operation, 51.9 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```

## Code explanation


- `sudo apt-get install apache2 php mysql-server` - This command will install Apache web server, PHP, and MySQL on the EC2 instance.
- `sudo apt-get install libapache2-mod-php` - This command will install the Apache module which enables Apache to recognize and serve PHP files.
- `sudo service apache2 restart` - This command will restart the Apache web server to apply the changes made by the previous command.
- `mysql -u root -p` - This command will log into the MySQL server as the root user.
- `CREATE DATABASE dbname;` - This command will create a database for your website.
- `CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';` - This command will create a MySQL user for your website.
- `GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';` - This command will grant the created user access to the database.

## Helpful links

- [Amazon EC2 Documentation](https://aws.amazon.com/documentation/ec2/)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

onelinerhub: [How do I host a PHP website on AWS?](https://onelinerhub.com/php-aws/how-do-i-host-a-php-website-on-aws)