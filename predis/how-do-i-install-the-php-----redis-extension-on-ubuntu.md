# How do I install the PHP 7.4 Redis extension on Ubuntu?
// plain

1. To install the PHP 7.4 Redis extension on Ubuntu, first you need to install the Redis server. To do this, run the following command in the terminal:
```
sudo apt-get install redis-server
```

2. Then, you need to install the prerequisite packages for building the PHP Redis extension. Run the following command in the terminal:
```
sudo apt-get install php7.4-dev php-pear
```

3. Next, you need to install the Redis extension for PHP. To do this, use the pecl command:
```
sudo pecl install redis
```

4. Once the installation is complete, you need to enable the extension in the php.ini file. To do this, open the php.ini file and add the following line:
```
extension=redis.so
```

5. Finally, restart the Apache web server for the changes to take effect. To do this, run the following command:
```
sudo service apache2 restart
```

6. To verify that the extension is installed correctly, you can run the following command:
```
php -m | grep redis
```
The output should look like this:
```
redis
```

7. For more information, please refer to the [PHP Redis Documentation](https://pecl.php.net/package/redis).

onelinerhub: [How do I install the PHP 7.4 Redis extension on Ubuntu?](https://onelinerhub.com/predis/how-do-i-install-the-php-----redis-extension-on-ubuntu)