# How do I set up PHP hosting on Amazon EC2?
// plain

1. Create an Amazon EC2 instance and configure it for hosting your PHP application. You can do this by following the [instructions provided by Amazon](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).

2. Install Apache web server, MySQL and PHP on your EC2 instance. This can be done by running the following command:

```
sudo yum install httpd24 php71 mysql57-server php71-mysqlnd
```

3. Start the Apache web server and MySQL server:

```
sudo service httpd start
sudo service mysqld start
```

4. Create a database and a user for your PHP application:

```
mysql -u root -p
CREATE DATABASE mydatabase;
CREATE USER myuser@localhost IDENTIFIED BY 'mypassword';
GRANT ALL ON mydatabase.* TO myuser@localhost;
FLUSH PRIVILEGES;
```

5. Configure Apache to serve your PHP application:

```
sudo vi /etc/httpd/conf/httpd.conf
```

Add the following lines to the end of the file:

```
Alias /myapp /var/www/html/myapp
<Directory /var/www/html/myapp>
    AllowOverride All
    Require all granted
</Directory>
```

6. Restart Apache web server:

```
sudo service httpd restart
```

7. Upload your PHP application to the EC2 instance and you are ready to go!

onelinerhub: [How do I set up PHP hosting on Amazon EC2?](https://onelinerhub.com/php-aws/how-do-i-set-up-php-hosting-on-amazon-ec-)