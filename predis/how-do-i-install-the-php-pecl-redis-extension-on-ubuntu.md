# How do I install the PHP PECL Redis extension on Ubuntu?
// plain

1. First, you need to install the Redis server on your Ubuntu machine. You can do this by running the following command in the terminal:
   ```
   sudo apt-get install redis-server
   ```
2. Next, you need to install the PHP development package, which will allow you to compile the PECL Redis extension. Run the following command in the terminal:
   ```
   sudo apt-get install php-dev
   ```
3. Now, you can install the PECL Redis extension. Run the following command in the terminal:
   ```
   sudo pecl install redis
   ```
   This will install the extension in your system.
4. After the extension has been installed, you need to enable it in your `php.ini` file. Open the `php.ini` file and add the following line:
   ```
   extension=redis.so
   ```
5. Finally, you need to restart your web server for the changes to take effect.
6. To verify that the extension is working correctly, you can run the following command in the terminal:
   ```
   php -m | grep redis
   ```
   This should output the following line:
   ```
   redis
   ```
7. You can find more information about installing the PECL Redis extension on [the official PHP documentation](http://php.net/manual/en/redis.installation.php).

onelinerhub: [How do I install the PHP PECL Redis extension on Ubuntu?](https://onelinerhub.com/predis/how-do-i-install-the-php-pecl-redis-extension-on-ubuntu)