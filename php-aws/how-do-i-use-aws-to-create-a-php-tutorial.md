# How do I use AWS to create a PHP tutorial?
// plain

1. First, you need to create an Amazon Web Services (AWS) account. You can do this by visiting [aws.amazon.com](https://aws.amazon.com/) and signing up for an account.
2. Once you have created your account, you can launch an EC2 instance. This is a virtual machine that will host your PHP tutorial. You can do this by going to the EC2 dashboard and clicking on "Launch Instance".
3. Next, you will need to install Apache, MySQL, and PHP on your instance. You can do this using `sudo apt-get install apache2 mysql-server php5`
4. Once the installation is complete, you can create your PHP tutorial files. You can do this using a text editor such as `nano` or `vim`.
5. Once your tutorial files are created, you will need to upload them to your EC2 instance. You can do this using the `scp` command. For example, `scp tutorial.php ec2-user@ec2-xx-xxx-xxx-xxx.compute-1.amazonaws.com:/var/www/html`
6. Now, you can view your tutorial files in your web browser. All you need to do is navigate to the IP address of your EC2 instance.
7. Finally, you can share your tutorial with others by providing them with the URL of your EC2 instance.

```
sudo apt-get install apache2 mysql-server php5
```

## Output example

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  apache2-bin apache2-data libapr1 libaprutil1 libaprutil1-dbd-sqlite3
  libaprutil1-ldap liblua5.1-0 libqdbm14 mysql-client-5.5
  mysql-client-core-5.5 mysql-common mysql-server-5.5
  mysql-server-core-5.5 php5-cli php5-common php5-json php5-readline
Suggested packages:
  apache2-doc apache2-suexec-pristine apache2-suexec-custom
  php-pear
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data libapr1 libaprutil1
  libaprutil1-dbd-sqlite3 libaprutil1-ldap liblua5.1-0 libqdbm14
  mysql-client-5.5 mysql-client-core-5.5 mysql-common mysql-server
  mysql-server-5.5 mysql-server-core-5.5 php5 php5-cli php5-common
  php5-json php5-readline
0 upgraded, 18 newly installed, 0 to remove and 0 not upgraded.
Need to get 28.3 MB of archives.
After this operation, 136 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```

onelinerhub: [How do I use AWS to create a PHP tutorial?](https://onelinerhub.com/php-aws/how-do-i-use-aws-to-create-a-php-tutorial)